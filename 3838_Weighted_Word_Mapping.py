from typing import List

LETTERS_TO_INDICES = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}

WEIGHTS_TO_LETTERS = {
    0: "z",
    1: "y",
    2: "x",
    3: "w",
    4: "v",
    5: "u",
    6: "t",
    7: "s",
    8: "r",
    9: "q",
    10: "p",
    11: "o",
    12: "n",
    13: "m",
    14: "l",
    15: "k",
    16: "j",
    17: "i",
    18: "h",
    19: "g",
    20: "f",
    21: "e",
    22: "d",
    23: "c",
    24: "b",
    25: "a"
}

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        wordWeights = [wordWeight(word, weights) for word in words]
        resultLetters = [WEIGHTS_TO_LETTERS[weight % 26] for weight in wordWeights]
        return "".join(resultLetters)


def wordWeight(word, weights):
    ans = 0
    for char in word:
        ans += weights[LETTERS_TO_INDICES[char]]
    return ans


s = Solution()

# words = ["abcd","def","xyz"]
# weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

words = ["a","b","c"]
weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

ans = s.mapWordWeights(words, weights)
print("ans:", ans)