from typing import List

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        
        while "%" in text:
            for pair in replacements:
                # print("pair:", pair)
                # print("before replacement:", text)
                charToReplace, newString = pair
                textToReplace = "%" + charToReplace + "%"
                text = text.replace(textToReplace, newString)
                # print("after replacement :", text)
        return text
        

s = Solution()

replacements = [["A","bce"],["B","ace"],["C","abc%B%"]]
text = "%A%_%B%_%C%"

s.applySubstitutions(replacements, text)