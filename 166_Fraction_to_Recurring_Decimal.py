class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator < 0 and denominator < 0:
            return self.fractionToDecimal(-1*numerator, -1*denominator)
        
        if numerator < 0 and denominator > 0:
            return "-" + self.fractionToDecimal(-1*numerator, denominator)
        
        if numerator > 0 and denominator < 0:
            return "-" + self.fractionToDecimal(numerator, -1*denominator)

        
        

        if (numerator/denominator) == (int(numerator/denominator)):
            return str(int(numerator/denominator))
        
        if numerator > denominator:
            whole_part = int(numerator/denominator)
            division_result, repeats = division(numerator-(whole_part*denominator), denominator)
            if repeats:
                decimal_part = process_string(division_result)
                ans = decimal_part.replace("0.", str(whole_part) + ".")
                return ans
            else:
                return str(numerator/denominator)
        elif numerator == denominator:
            return "1"
        else:

            unprocessed_result, repeats, repeat_depth = division(numerator, denominator)
            print("unprocessed_result:", unprocessed_result)
            print("repeats:", repeats)
            print("repeat_depth:", repeat_depth)
            input()
            if repeats:
                ans = process_string(unprocessed_result)
            else:
                ans = "0."+unprocessed_result[1:]
            return ans


def dict_contains_nonzero(d):
    if len(d) == 0:
        return False
    for key in d.keys():
        if key != "0":
            return True
    return False

def process_string(unprocessed):
    repeater = unprocessed[-1]
    after_decimal = unprocessed[1:]
    
    for i, char in enumerate(after_decimal):
        if char == repeater:
            repeat_index = i
            break
    if repeat_index == len(after_decimal)-1:
        repeated_part = after_decimal[-1]
    else:
        repeated_part = after_decimal[repeat_index:-1]

    ans = after_decimal[0:repeat_index] + "(" + repeated_part + ")"
    return "0." + ans
            

def division(numerator, denominator):
    answer, repeats, repeat_depth = divisionHelper(numerator, denominator, {}, 0)
    return answer, repeats, repeat_depth


def divisionHelper(numerator, denominator, seen_before, depth):
    # print("numerator:", numerator)
    # print("denominator:", denominator)
    # print()
    state = (numerator, denominator)
    if state in seen_before:
        return str(int(numerator/denominator)), True, seen_before[state]
    seen_before[state] = depth
    
    digits_so_far = ""
    while numerator < denominator:
        digits_so_far += "0"
        numerator *= 10
    
    top_part = int(numerator/denominator)
    digits_so_far += str(top_part)
    product = top_part*denominator
    remainder = numerator - product

    if remainder == 0:
        return digits_so_far, False, -1
    else:
        remaining_string, repeats, repeat_depth = divisionHelper(remainder*10, denominator, seen_before, depth+1)
        return digits_so_far + remaining_string, repeats, repeat_depth
    


# a = division(-50,8)
# print(a)

mySol = Solution()

ans = mySol.fractionToDecimal(1, 7)
print(ans)