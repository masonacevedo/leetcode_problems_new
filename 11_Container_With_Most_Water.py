from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        bestSoFar = float('-inf')
        while left != right:
            # print("left:", left)
            # print("right:", right)
            # print("bestSoFar:", bestSoFar)
            # input()
            lHeight = height[left]
            rHeight = height[right]
            area = min(lHeight, rHeight)*(right-left)
            bestSoFar = max(bestSoFar, area)

            if lHeight < rHeight:
                left += 1
            else:
                right -= 1
        return bestSoFar

mySol = Solution()
h = [1,8,6,2,5,4,8,3,7]
mySol.maxArea(h)