from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        totalTargets = nums.count(target)
        # print("nums:")
        # print(nums)
        prefixCounts = [0]
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                count += 1
            prefixCounts.append(count)
        

        suffixCounts = [0]
        count = 0
        for i in reversed(range(0, len(nums))):
            if nums[i] == target:
                count += 1
            suffixCounts.append(count)
        suffixCounts = list(reversed(suffixCounts))
        ans = 0
        # print("prefixCounts:")
        # print(prefixCounts)
        # print("suffixCounts:")
        # print(suffixCounts)
        # breakpoint()
        for i in range(0, len(nums)):
            for j in range(i, len(nums)+1):
                # print("subarray:")
                # print(nums[i:j])
                # print("potential answer?")
                # print(totalTargets - prefixCounts[i] - suffixCounts[j])
                # print("array length:")
                # print(j - i)
                numTargets = totalTargets - prefixCounts[i] - suffixCounts[j]
                if numTargets > ((j-i)//2):
                    ans += 1
                #     print("increasing ans!")
                # else:
                #     print("not increasing ans...")
                
                
                # breakpoint()


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