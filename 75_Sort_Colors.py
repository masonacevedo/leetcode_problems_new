from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        one_count = nums.count(1)
        two_count = nums.count(2)

        nums[0:zero_count] = [0]*zero_count
        nums[zero_count: zero_count+one_count] = [1]*one_count
        nums[zero_count+one_count:zero_count+one_count + two_count] = [2]*two_count
        return nums