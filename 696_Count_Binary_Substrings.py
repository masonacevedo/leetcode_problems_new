class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        ans = 0
        while i < len(s)-1:
            current_char = s[i]
            next_char = s[i+1]

            if current_char != next_char:
                num = calculateSplitSize(s, i, i+1)
                ans += num
            i += 1
        return ans
    
def calculateSplitSize(s, i1, i2):
    initialLeftChar = s[i1]
    initialRightChar = s[i2]
    leftChar = s[i1]
    rightChar = s[i2]

    ans = 0
    while i2 < len(s) and i1 >= 0:
        leftChar = s[i1]
        rightChar = s[i2]
        if leftChar == initialLeftChar and rightChar == initialRightChar:
            ans += 1
        else:
            break

        
        i1 -= 1
        i2 += 1
        
    return ans
        

mySol = Solution()#                0123456
ans = mySol.countBinarySubstrings("1010001")
print("final ans:", ans)