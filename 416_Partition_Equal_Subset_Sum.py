from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        return subsetSum(nums, sum(nums)//2, memo={})


def subsetSum(nums, target, memo):
    if len(nums) == 1:
        return nums[0] == target
    
    if target < 0:
        return False
    
    

    key = (tuple(nums), target)
    if key in memo:
        return memo[key]
    

    firstNum = nums[0]

    useIt = subsetSum(nums[1:], target - firstNum, memo)
    loseIt = subsetSum(nums[1:], target, memo)
    ans = (useIt or loseIt)
    memo[key] = ans
    return ans

s = Solution()
nums = [20,68,68,11,48,18,50,5,3,51,52,11,13,11,38,100,30,87,1,56,85,63,14,96,7,17,54,11,32,61,94,13,85,10,78,57,69,92,66,28,70,20,3,29,10,73,89,86,28,48,69,54,87,11,91,32,59,4,88,20,81,100,29,75,79,82,6,74,66,30,9,6,83,54,54,53,80,94,64,77,22,7,22,26,12,31,23,26,65,65,35,36,34,1,12,44,22,73,59,99]

ans = s.canPartition(nums)
print("ans:", ans)