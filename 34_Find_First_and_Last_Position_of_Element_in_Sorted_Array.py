from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        knownIndex = normalSearch(nums, target)
        if knownIndex == -1:
            return [-1, -1]
        if len(nums) < 4:
            if not(target in nums):
                return [-1, -1]
            firstOccurence = nums.index(target)
            lastOccurence = len(nums) - list(reversed(nums)).index(target) - 1
            return [firstOccurence, lastOccurence]
        
        if knownIndex == 0:
            return [0,0]
        elif knownIndex == len(nums) - 1:
            return [len(nums)-1, len(nums)-1]
        # print("knownIndex:", knownIndex)
        lowerHalf = specialSearch(nums[0:knownIndex], target, "lower")
        upperHalf = specialSearch(nums[knownIndex:], target, "upper")
        return [lowerHalf, knownIndex + upperHalf]

def specialSearch(nums, target, upperOrLower):
    if upperOrLower == "upper" and max(nums) == target:
        return len(nums) - 1
    elif upperOrLower == "lower" and min(nums) == target:
        return 0
    
    upperBound = len(nums)
    lowerBound = 0

    while (lowerBound + 1) != upperBound:
        
        middleIndex = (upperBound + lowerBound)//2
        guess = nums[middleIndex]

        if upperOrLower == "upper":
            # print("middleIndex:", middleIndex)
            # print("guess:", guess)
            # print()
            if guess == target:
                lowerBound = middleIndex
            else:
                upperBound = middleIndex
        else:
            # print("uppe")
            # print("middleIndex:", middleIndex)
            # print("guess:", guess)
            # print()
            if guess == target:
                upperBound = middleIndex
            else:
                lowerBound = middleIndex
    
    if upperOrLower == "upper":
        return lowerBound
    else:
        return upperBound


def normalSearch(nums, target):
    # print("nums:", nums)
    if len(nums) == 0:
        return -1
    elif len(nums) == 1:
        return 0 if target in nums else -1
    
    middleIndex = len(nums)//2
    
    if target > nums[middleIndex]:
        recursiveCall = normalSearch(nums[middleIndex:], target)
        if recursiveCall == -1:
            return -1
        
        return middleIndex + recursiveCall
    elif target < nums[middleIndex]:
        return normalSearch(nums[0:middleIndex], target)
    else:
        return middleIndex



nums = [0,1,1,1,1,2,2,2,3,3,3,3,4,5,6,6,8,9,9,9]



target = 0
s = Solution()
ans = s.searchRange(nums, target)
print("ans:", ans)