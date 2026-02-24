class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        inSubstring = {s[0]: 0}
        bestSoFar = 1
        current_substring = s[0]
        while right < len(s) and left < len(s):
            leftChar = s[left]
            rightChar = s[right]
            if rightChar in current_substring:
                doubledCharIndex = left + current_substring.index(rightChar)
                left = doubledCharIndex + 1
                current_substring = s[left:left+1]
                right = left+1
            else:
                bestSoFar = max(bestSoFar, right - left + 1)
                current_substring += rightChar
                right += 1

        return bestSoFar 

mySol = Solution()

assert(mySol.lengthOfLongestSubstring("pwwkew") == 3)
assert(mySol.lengthOfLongestSubstring("bbbbbb") == 1)
assert(mySol.lengthOfLongestSubstring("abcabcbb") == 3)
assert(mySol.lengthOfLongestSubstring("tmmzuxt") == 5)
assert(mySol.lengthOfLongestSubstring("aabaab!bb") == 3)