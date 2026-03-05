
import random

add = {

    ("0","0"): ("0", "0"),
    ("0","1"): ("0", "1"),
    ("0","2"): ("0", "2"),
    ("0","3"): ("0", "3"),
    ("0","4"): ("0", "4"),
    ("0","5"): ("0", "5"),
    ("0","6"): ("0", "6"),
    ("0","7"): ("0", "7"),
    ("0","8"): ("0", "8"),
    ("0","9"): ("0", "9"),


    ("1","1"): ("0", "2"),
    ("1","2"): ("0", "3"),
    ("1","3"): ("0", "4"),
    ("1","4"): ("0", "5"),
    ("1","5"): ("0", "6"),
    ("1","6"): ("0", "7"),
    ("1","7"): ("0", "8"),
    ("1","8"): ("0", "9"),
    ("1","9"): ("1", "0"),

    ("2","2"): ("0", "4"),
    ("2","3"): ("0", "5"),
    ("2","4"): ("0", "6"),
    ("2","5"): ("0", "7"),
    ("2","6"): ("0", "8"),
    ("2","7"): ("0", "9"),
    ("2","8"): ("1", "0"),
    ("2","9"): ("1", "1"),

    ("3","3"): ("0", "6"),
    ("3","4"): ("0", "7"),
    ("3","5"): ("0", "8"),
    ("3","6"): ("0", "9"),
    ("3","7"): ("1", "0"),
    ("3","8"): ("1", "1"),
    ("3","9"): ("1", "2"),

    ("4","4"): ("0", "8"),
    ("4","5"): ("0", "9"),
    ("4","6"): ("1", "0"),
    ("4","7"): ("1", "1"),
    ("4","8"): ("1", "2"),
    ("4","9"): ("1", "3"),

    ("5","5"): ("1", "0"),
    ("5","6"): ("1", "1"),
    ("5","7"): ("1", "2"),
    ("5","8"): ("1", "3"),
    ("5","9"): ("1", "4"),

    ("6","6"): ("1", "2"),
    ("6","7"): ("1", "3"),
    ("6","8"): ("1", "4"),
    ("6","9"): ("1", "5"),

    ("7","7"): ("1", "4"),
    ("7","8"): ("1", "5"),
    ("7","9"): ("1", "6"),

    ("8","8"): ("1", "6"),
    ("8","9"): ("1", "7"),

    ("9","9"): ("1", "8"),

}

increment = {
    "0":"1",
    "1":"2",
    "2":"3",
    "3":"4",
    "4":"5",
    "5":"6",
    "6":"7",
    "7":"8",
    "8":"9",
}

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a > b:
            bigger, smaller = a,b
        else:
            bigger, smaller = b,a 
        
        
        bigStr = str(bigger)
        smallStr = str(smaller)
        
        fillerZeros = "0" * (len(bigStr) - len(smallStr))
        smallStr = fillerZeros + smallStr
        
        i = len(bigStr)-1
        ans = ""
        carryOne = False
        while i >= 0:
            topDigit = bigStr[i]
            bottomDigit = smallStr[i]

            # print("i:", i)
            # print("top:", topDigit)
            # print("bot:", bottomDigit)
            
            pair = tuple(list(sorted([topDigit, bottomDigit])))
            
            if carryOne:
                partialResult = add[pair]
                sumResult = addOne(partialResult)
            else:
                sumResult = add[pair]

            
            if sumResult[0] == "1":
                carryOne = True
            else:
                carryOne = False

            ans += sumResult[1]

            i -= 1
        
        if carryOne:
            ans += "1"
        
        reversedAns = "".join(list(reversed(ans)))
        # print("reversedAns:", reversedAns)
        return int(reversedAns)


def addOne(pair):
    if pair == ("0", "9"):
        return ("1", "0")
    elif pair == ("1", "9"):
        raise Exception("Invalid!!")
    else:
        return (pair[0] + increment[pair[1]])

s = Solution()

# 64367
#   947
#     

# s.getSum(64367, 947)
# a = 64367
# b
# assert()

for _ in range(0, 10000):
    a = random.randint(1, 999999)
    b = random.randint(1, 999999)
    print(a, " + ", b)

    assert(a + b == s.getSum(a,b))