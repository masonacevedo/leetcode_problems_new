from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # if 
        sortedArr = sorted(arr)
        

        diff = sortedArr[1]-sortedArr[0]

        for i in range(1, len(arr)-1):
            n1 = sortedArr[i]
            n2 = sortedArr[i+1]

            if (n2 - n1) != diff:
                return False
        return True

s = Solution()

arr = [-68,-96,-12,-40,16]
s.canMakeArithmeticProgression(arr)