class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleaveHelper(s1, s2, s3)
    
    def isInterleaveHelper(self, s1, s2, s3, memo = None):
        strings = [s1,s2,s3]
        # breakpoint()
        if memo is None:
            memo = {}

        memoKey = tuple([s1, s2, s3])
        # print("memoKey:", memoKey)
        # print("memo:", memo)
        # print()
        if memoKey in memo:
            # print("using memo!")
            return memo[memoKey]

        if len(s1) + len(s2) != len(s3):
            return False
        
        if s1 == "":
            return s2 == s3
        
        if s2 == "":
            return s1 == s3
        
        # print("going to try peel 1")
        # breakpoint()
        if s1[0] == s3[0]:
            peel_1 = self.isInterleaveHelper(s1[1:], s2, s3[1:], memo)
            if peel_1:
                # print("peel 1 worked")
                # breakpoint()
                # print("added to memo?")
                memo[memoKey] = True
                return True
        # print("going to try peel 2")
        # breakpoint()
        if s2[0] == s3[0]:
            peel_2 = self.isInterleaveHelper(s1, s2[1:], s3[1:], memo)
            if peel_2:
                # print("peel2 worked")
                # breakpoint()
                # print('added to memo?')
                memo[memoKey] = True
                return True
        # print("neither peel worked")
        # breakpoint()
        memo[memoKey] = False
        # print("added to memo?")
        return False

s = Solution()
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"

s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
assert(not(s.isInterleave(s1, s2, s3)))

