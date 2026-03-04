from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return robHelper(nums, memo={})

def robHelper(nums, memo):
    if tuple(nums) in memo:
        return memo[tuple(nums)]
    elif len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    
    loseIt = robHelper(nums[1:], memo)
    useIt = nums[0] + robHelper(nums[2:], memo)
    ans = max(useIt, loseIt)
    memo[tuple(nums)] = ans
    return ans



nums = [1,2,3,1]
mySol = Solution()
ans = mySol.rob(nums)
print("ans:", ans)