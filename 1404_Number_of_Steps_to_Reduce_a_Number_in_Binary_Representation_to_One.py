import copy
class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        while s != "1":
            if s[-1] == "0":
                s = s[0:-1]
            else:
                s = increment(s)
            count += 1
        return count

def increment(s):
    if s[-1] == "0":
        return s[0:-1] + "1"
    
    i = len(s)-1
    foundZero = False
    while i > 0:
        char = s[i]
        if char == "0":
            foundZero = True
            break
        i -= 1

    if foundZero:
        return s[0:i] + "1" + "0"*(len(s)-i-1)
    else:
        return "1" + "0"*len(s)



mySol = Solution()
ans = mySol.numSteps("1101")
print(ans)

# i = 0
# s = "1"
# while i < 128:
#     print(s)
#     input()
#     s= increment(s)

    