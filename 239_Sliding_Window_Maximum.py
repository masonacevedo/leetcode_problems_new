from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque([])
        for i in range(0, k):
            window.append(nums[i])
        
        ans = [max(window)]
        for i in range(k, len(nums)):
            window.popleft()
            window.append(nums[i])
            ans.append(max(window))
        return ans


mySol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
ans = mySol.maxSlidingWindow(nums, k)
print("ans:", ans)