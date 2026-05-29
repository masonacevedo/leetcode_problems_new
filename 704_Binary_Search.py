from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lower = 0
        upper = len(nums)-1

        while (upper - lower) > 1:

            middleIndex = (lower + upper)//2
            if nums[middleIndex] == target:
                return middleIndex
            elif nums[middleIndex] > target:
                upper = middleIndex
            else:
                lower = middleIndex
        
        if nums[upper] == target:
            return upper
        elif nums[lower] == target:
            return lower
        return -1

nums = [-1,0,3,5,9,12]
target = 2

# nums = [-1,0,3,5,9,12]
# target = 12

s = Solution()

ans = s.search(nums, target)
print("ans:", ans)