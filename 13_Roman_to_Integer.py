specialCase = {
    ("I","V"): 4,
    ("I","X"): 9,
    ("X","L"): 40,
    ("X","C"): 90,
    ("C","D"): 400,
    ("C","M"): 900,
}

normalCase = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        index = 0
        while index < len(s):
            if index == 0:
                ans += normalCase[s[index]]
            else:
                currentChar = s[index]
                prevChar = s[index-1]
                if normalCase[currentChar] > normalCase[prevChar]:
                    ans -= normalCase[prevChar]
                    ans += specialCase[(prevChar, currentChar)]
                else:
                    ans += normalCase[currentChar]

            index += 1
        return ans
                