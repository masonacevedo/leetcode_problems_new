from typing import List
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        
        smallerSubsets = self.subsets(nums[1:])
        ans = []
        for smallerSubset in smallerSubsets:
            without = copy.copy(smallerSubset)
            ans.append(without)
            withNum = copy.copy(smallerSubset)
            withNum.append(nums[0])
            ans.append(withNum)
        return ans

mySol = Solution()
nums = [1,2,3]
ans = mySol.subsets(nums)
print("ans:", ans)