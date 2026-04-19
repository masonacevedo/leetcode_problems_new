from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        right = 0
        left = 0

        best_so_far = 0

        while left < len(nums1) and right < len(nums2):
            num1 = nums1[left]
            num2 = nums2[right]

            if num1 <= num2:
                best_so_far = max(best_so_far, right - left)

            if num2 >= num1:
                right += 1
            else:
                left += 1


        return best_so_far



s = Solution()
# nums1 = [55,30,5,4,2]
# nums2 = [100,20,10,10,5]
nums1 = [2, 2, 2]
nums2 = [10, 10, 1]

# nums1 = [30,29,19,5]
# nums2 = [25,25,25,25,25]

ans = s.maxDistance(nums1, nums2)
print("ans:", ans)