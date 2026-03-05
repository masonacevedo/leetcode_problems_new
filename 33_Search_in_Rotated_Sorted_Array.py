# idea: first, conduct binary search to see where
#  the "pivot" point is. 
# then, once we know that, binary search the half before the pivot,
# and binary search the half after the pivot. 
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        elif len(nums) == 2:
            return nums.index(target) if target in nums else -1
        leftBound, rightBound = locatePivot(nums)
        # print("leftBound:", leftBound)
        # print("rightBound:", rightBound)
        if (leftBound, rightBound) == (-1, -1):
            return regularSearch(nums, target)
        
        leftArray = nums[0:leftBound+1]
        rightArray = nums[rightBound:]
        # print("leftArray:", leftArray)

        # print("rightArray:", rightArray)
        leftSearchResult = regularSearch(leftArray, target)
        rightSearchResult = regularSearch(rightArray, target)

        # print("leftRes:", leftSearchResult)
        # print("rightRes:", rightSearchResult)
        
        if leftSearchResult == -1 and rightSearchResult == -1:
            return -1

        # cute way to return NOT -1.
        if leftSearchResult != -1:
            return leftSearchResult
        
        return rightBound + rightSearchResult


def regularSearch(nums, target):
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    elif len(nums) == 2:
        return nums.index(target) if target in nums else -1
    lowerBound = 0
    upperBound = len(nums)-1

    guess = (lowerBound + upperBound)//2
    while lowerBound+1 != upperBound:
        # print("upper:", upperBound)
        # print("lower:", lowerBound)
        # print("guess:", guess)
        # print("lowreBound + upperBound//2:", (upperBound+lowerBound)//2)
        # print()
        # input()

        curNum = nums[guess]
        if curNum == target:
            return guess
        elif curNum > target:
            upperBound = guess
        else:
            lowerBound = guess
        guess = (lowerBound + upperBound)//2
    
    if nums[lowerBound] == target:
        return lowerBound
    elif nums[upperBound] == target:
        return upperBound
    else:
        return -1
        

def locatePivot(nums):
    lowerBound = 0
    upperBound = len(nums)-1

    guess = (lowerBound + upperBound)//2

    while lowerBound + 1 != upperBound:
        # print("upper:", upperBound)
        # print("lower:", lowerBound)
        # print("guess:", guess)
        # print()

        leftNum = nums[lowerBound]
        rightNum = nums[upperBound]
        midNum = nums[guess]

        if leftNum < midNum:
            lowerBound = guess
        else:
            upperBound = guess
        guess = (lowerBound + upperBound)//2
    
    # print("len(nujms:)", len(nums))
    # print("upper:", upperBound)
    # print("lower:", lowerBound)
    # print("guess:", guess)
    # print()
    if upperBound == len(nums)-1:
        # print("aaaaa")
        if nums[lowerBound] < nums[upperBound]:
            # print("bbb")
            return -1, -1
    # print("cccc")
    return lowerBound, upperBound


s = Solution()
nums = [3,5,1]
# nums = [1,2,3,4,5,6,-1]
target = 0
ans = s.search(nums, target)
print("ans:", ans)