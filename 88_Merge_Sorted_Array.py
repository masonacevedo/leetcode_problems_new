from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(0, len(nums1)):
                nums1[i] = nums2[i]
            return
        
        i1 = 0
        i2 = 0

        newArray = []
        while i1 < m and i2 < n:
            num1 = nums1[i1]
            num2 = nums2[i2]
            smaller = num1 if num1 < num2 else num2
            newArray.append(smaller)
            if smaller == num1:
                i1 += 1
            else:
                i2 += 1
        
        if i1 == m:
            while i2 < n:
                newArray.append(nums2[i2])
                i2 += 1
            
        elif i2 == n:
            while i1 < m+n:
                newArray.append(nums1[i1])
                i1 += 1
            
        for i in range(0, len(nums1)):
            nums1[i] = newArray[i]
            

mySol = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
mySol.merge(nums1, m, nums2, n)


