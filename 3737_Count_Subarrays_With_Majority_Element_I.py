from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)+1):
                subarray = nums[i:j]
                if majorityMatch(subarray, target):
                    ans += 1
        return ans

def majorityMatch(subarray, target):
    targetCount = 0
    for num in subarray:
        if target == num:
            targetCount += 1
    return (targetCount) > (len(subarray)//2)


nums = [1,2,2,3]
target = 2

s = Solution()
ans = s.countMajoritySubarrays(nums, target)
print("ans:", ans)