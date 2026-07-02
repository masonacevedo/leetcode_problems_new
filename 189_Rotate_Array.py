class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newNums = [None for i in range(0, len(nums))]

        for i in range(0, len(nums)):
            newIndex = (i + k)%(len(nums))
            newNums[newIndex] = nums[i]
        
        for i in range(0, len(nums)):
            nums[i] = newNums[i]
