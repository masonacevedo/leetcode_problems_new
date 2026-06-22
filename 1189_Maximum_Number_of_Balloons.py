class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonChars = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }
        for char in text:
            if char in balloonChars:
                balloonChars[char] += 1
        
        singleChars = ["b", "a", "n"]
        singleOccurences = [count for char, count in balloonChars.items() if char in singleChars]
        doubleChars = ["l", "o"]
        doubleOccurences = [count//2 for char, count in balloonChars.items() if char in doubleChars]
        return min(min(singleOccurences), min(doubleOccurences))


s = Solution()

text = "leetcode"

ans = s.maxNumberOfBalloons(text)
print("ans:", ans)