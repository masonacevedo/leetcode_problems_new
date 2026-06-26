
import copy
LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        positions = {}
        for i,char in enumerate(s):
            if char in positions:
                positions[char].append(i)
            else:
                positions[char] = [i]
        
        removeChars = set()
        for letter in reversed(LETTERS):
            if letter not in positions:
                continue
            
            for pos in positions[letter][0:-1]:
                removeChars.add(pos)

        ans = []
        for i in range(0, len(s)):
            if i not in removeChars:
                ans.append(s[i])
        
        return "".join(ans)

        



sol = Solution()
s = "bcabc"
ans = sol.removeDuplicateLetters(s)
print("ans:", ans)