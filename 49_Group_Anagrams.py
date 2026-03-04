from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansDict = {}
        for s in strs:
            anagramDict = calcAnagramDict(s)
            if anagramDict in ansDict:
                ansDict[anagramDict].append(s)
            else:
                ansDict[anagramDict] = [s]
        return list(ansDict.values())


def calcAnagramDict(s):
    ans = {}
    for char in s:
        if char in ans:
            ans[char] += 1
        else:
            ans[char] = 1
    print(tuple(sorted(ans.items())))
    return tuple(sorted(ans.items()))

mySol = Solution()
# strings = ["ddddddddddg","dgggggggggg"]
strings = ["eat","tea","tan","ate","nat","bat"]
ans = mySol.groupAnagrams(strings)
print("ans:", ans)