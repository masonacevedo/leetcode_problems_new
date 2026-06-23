from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        remainingPerms = self.permute(nums[1:])

        ans = []
        for p in remainingPerms:
            for i in range(0, len(p)):
                newPerm = p[0:i] + [nums[0]] + p[i:]
                ans.append(newPerm)
            newPerm = p + [nums[0]]
            ans.append(newPerm)
        return ans

s = Solution()

nums = [1,2,3,4]
ans = s.permute(nums)

for permutation in ans:
    print(permutation)