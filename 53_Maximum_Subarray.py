from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        bestSoFar = float('-inf')

        for num in nums:
            # print("num:", num)
            # print("currentSum:", currentSum)
            # print("bestSoFar:", bestSoFar)
            # input()
            currentSum += num
            bestSoFar = max(bestSoFar, currentSum)
            if currentSum < 0:
                currentSum = 0
        
        return bestSoFar
mySol = Solution()

nums = [5,4,-1,7,8]

ans = mySol.maxSubArray(nums)
print("ans:", ans)