from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenBefore = {}
        for i, num in enumerate(nums):
            if num in seenBefore:
                return [i, seenBefore[num]]
            else:
                seenBefore[target - num] = i


mySol = Solution()

mySol.twoSum(nums = [2,7,11,15], target = 9)
