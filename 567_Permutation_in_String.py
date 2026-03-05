class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapping = buildMapping(s1)
        
        for i in range(0, len(s2)-len(s1)+1):            
            if i == 0:
                subStr = s2[i:i+len(s1)]
                subStrMapping = buildMapping(subStr)
            else:
                prevChar = s2[i-1]

                subStrMapping[prevChar] -= 1
                if subStrMapping[prevChar] == 0:
                    del subStrMapping[prevChar]
                
                newChar = s2[i + len(s1)-1]
                
                if newChar in subStrMapping:
                    subStrMapping[newChar] += 1
                else:
                    subStrMapping[newChar] = 1
            
            if mapping == subStrMapping:
                return True
        return False

        

def buildMapping(s):
    mapping = {}
    for char in s:
        if char in mapping:
            mapping[char] += 1
        else:
            mapping[char] = 1
    return mapping


s1 = "oao"
s2 = "eidbaooo"

sol = Solution()
ans = sol.checkInclusion(s1, s2)
print("ans:", ans)