from typing import List
import copy

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        
        while "%" in text:
            for pair in replacements:
                # print("pair:", pair)
                # print("before replacement:", text)
                charToReplace, newString = pair
                textToReplace = "%" + charToReplace + "%"
                text = manualReplace(textToReplace, newString, text)
                # print("after replacement :", text)
        return text

def manualReplace(targetText, newText, bigString):
    ans = copy.copy(bigString)
    while targetText in ans:
        ans = replaceFirstInstance(targetText, newText, ans)
    return ans

def replaceFirstInstance(targetText, newText, bigString):
    ans = copy.copy(bigString)
    for i in range(0, len(bigString) - len(targetText)+1):
        potentialMatchingSubstring = bigString[i:i + len(targetText)]
        if potentialMatchingSubstring == targetText:
            ans = ans[0:i] + newText + ans[i+len(targetText):]
            return ans

# replacement = manualReplace("ab", "cdef", "ALDKRJHGIOWUHG|ab|ASD;LFGHPQOREGH|ab|ALKDFJHGKLQHRGT")    
# print("replacement:", replacement)
s = Solution()

replacements = [["A","bce"],["B","ace"],["C","abc%B%"]]
text = "%A%_%B%_%C%"

s.applySubstitutions(replacements, text)