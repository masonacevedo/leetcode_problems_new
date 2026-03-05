from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return robDP(nums)

def robDP(nums):
    DP = [nums[0], max(nums[0:2])]
    # print("nums:", nums)

    for i in range(2, len(nums)):
        useIt = nums[i] + DP[i-2]
        loseIt = DP[i-1]
        # print("DP:", DP)
        # print("useIt:", useIt)
        # print("loseIt:", loseIt)
        DP.append(max(useIt, loseIt))
    # print("DP:", DP)
    return DP[-1]

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



nums = [2,1,1,2]
mySol = Solution()
ans = mySol.rob(nums)
print("ans:", ans)