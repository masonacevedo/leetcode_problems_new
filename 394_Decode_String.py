numbers = [str(i) for i in range(0, 10)]
class Solution:
    def decodeString(self, s: str) -> str:
        return decodeStringHelper(s)


def decodeStringHelper(s):
    if len(s) == 0:
        return ""

    firstChar = s[0]
    if not(firstChar in numbers):
        ans = firstChar + decodeStringHelper(s[1:])
    else:
        # first character is a number
        numDigits = 0
        j = 0
        while j <= 2:
            if s[j] in numbers:
                numDigits += 1
            else:
                break
            j += 1
        

        # print("numDigits:", numDigits)
        mult = int(s[0:numDigits])
        # print("mult:", mult)

        
        bracketStack = ["["]
        i = numDigits+1
        # print("s:", s)
        # print("i:", i)
        # print("s[i]:", s[i])
        # print()
        while i < len(s) and len(bracketStack) > 0:
            char = s[i]
            
            if char == "[":
                bracketStack.append("[")
            elif char == "]":
                bracketStack.pop()
            i+= 1
        innerString = s[numDigits:i][1:-1]
        outerString = s[i:]
        # print("innerString:", innerString)
        # print("outerString:", outerString)
        # print()
        recursiveCallInner = decodeStringHelper(innerString)
        recursiveCallOuter = decodeStringHelper(outerString)
        ans = mult * recursiveCallInner + recursiveCallOuter
    return ans

mySol = Solution()
s = "10[a]2[bc]"
ans = mySol.decodeString(s)
print("final ans:", ans)