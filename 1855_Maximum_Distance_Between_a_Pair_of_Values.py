from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        right = len(nums2)-1
        left = 0

        while (right >= 0) and (left < len(nums1)):

            
            
            num2 = nums2[right]
            num1 = nums1[left]

            print("left: ", left)
            print("right:", right)
            print("num1:", num1)
            print("num2:", num2)
            input()

            if num1 <= num2:
                return right - left
            
            elif right == left:
                return 0
            
            else:

                num2Neighbor = nums2[right - 1]
                num1Neighbor = nums1[left + 1]

                if abs(num2 - num2Neighbor) > abs(num1 - num1Neighbor):
                    right -= 1
                else:
                    left += 1
        
        return 0



s = Solution()
# nums1 = [55,30,5,4,2]
# nums2 = [100,20,10,10,5]
# nums1 = [2, 2, 2]
# nums2 = [10, 10, 1]

nums1 = [30,29,19,5]
nums2 = [25,25,25,25,25]

ans = s.maxDistance(nums1, nums2)
print("ans:", ans)