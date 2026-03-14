from typing import List
import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = generateAllPartitions(s)
        # print("partitions:", partitions)
        ans = []
        for p in partitions:
            if all(isPalindrome(s) for s in p):
                ans.append(p)
        return ans

def generateAllPartitions(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [[s]]
    elif len(s) == 2:
        return [[s[0], s[1]], [s]]
    
    afterFirst = generateAllPartitions(s[1:])
    
    ans = []
    firstChar = s[0]
    for p in afterFirst:
        firstCharSeparate = [firstChar] + copy.deepcopy(p)
        firstCharJoin = [firstChar + copy.deepcopy(p[0])] + copy.deepcopy(p[1:])
        ans.append(firstCharSeparate)
        ans.append(firstCharJoin)
    return ans

def isPalindrome(s):
    return s == "".join(list(reversed(s)))

s = Solution()

# finalAns = s.partition("racecarracecar")
# print("finalAns:", finalAns)