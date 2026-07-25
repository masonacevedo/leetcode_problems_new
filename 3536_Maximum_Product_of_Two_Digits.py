class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        nums = [int(c) for c in s]

        ans = float("-inf")
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                ans = max(ans, nums[i]*nums[j])

        return ans

n = 1234

sol = Solution()

sol.maxProduct(n)