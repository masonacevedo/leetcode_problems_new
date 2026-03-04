from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSums = []

        for i in range(0, len(nums)+1):
            # print("nums[0:i]:")
            # print(nums[0:i])
            # input()
            self.prefixSums.append(sum(nums[0:i]))
        
        # print("prefixSums:", self.prefixSums)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSums[right+1]-self.prefixSums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

nums = [-2,0,3,-5,2,-1]

# [0,2],[2,5],[0,5]
myArray = NumArray(nums)
print(myArray.sumRange(0,2))
print(myArray.sumRange(2,5))
print(myArray.sumRange(0,5))
