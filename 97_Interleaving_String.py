class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        elif len(s3) == 0:
            return False

        s1Char = s1[0]
        s2Char = s2[0]

        if (s1[0] != s3[0]) and (s2[0] != s3[0]):
            return False
        elif (s1[0] == s3[0]) and (s2[0] != s3[0]):
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif (s1[0] != s3[0]) and (s2[0] == s3[0]):
            return self.isInterleave(s1, s2[1:], s3[1:])
        else:
            useS1 = self.isInterleave(s1[1:], s2, s3[1:])
            if useS1:
                return True            
            useS2 = self.isInterleave(s1, s2[1:], s3[1:])
            if useS2:
                return True
