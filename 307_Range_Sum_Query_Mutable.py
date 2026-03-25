# options: 
#  1. Actually update the array when we receive an update, actually compute entire sum range
#       update: O(1)
#       sumRange: O(n)
#  2. Maintain prefix sums starting from the beginning and ending. When update comes through, update all the prefix sums: 
#       update: O(n)
#       sumRange: O(1)
#  3. Maintain prefix sums starting from the beginning and ending. When sumRange request comes through, iterate through previous updates to adjust to appropriate number. 
#       update: O(1)
#       sumrange: O(k), where k is number of updates
#  4. Initialize all n^2 of the possible sumRanges on init. When update comes through, change the appropriate sumranges. 
#       update: O(n^2)
#       sumrange: O(1)
#  Better Options:
#       Use a "Segment Tree" or a Square Root Decomposition!
from typing import List

class Node:
    def __init__(self, val, leftChild=None, rightChild=None):
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def __repr__(self, c=1):
        ans = ""
        ans += str(self.val)
        if self.leftChild:
            ans += "\n"
            ans += c*"   "

            # ans += "left:"
            ans += self.leftChild.__repr__(c+1)
        if self.rightChild:
            ans += "\n"
            ans += c*"   "
            # ans += "right:"
            ans += self.rightChild.__repr__(c+1)
        return ans

class NumArray:

    def __init__(self, nums: List[int]):
        self.totalNums = len(nums)
        self.root = buildTree(nums)
        

    def update(self, index: int, val: int) -> None:
        nodesToUpdate = findNodesToUpdate(self.root, index, 0, self.totalNums)
        leafVal = nodesToUpdate[0].val
        difference = val - leafVal
        for n in nodesToUpdate:
            n.val += difference

    def sumRange(self, left: int, right: int) -> int:
        return getRange(self.root, left, right)
    
    def __repr__(self):
        return str(self.root)

def findNodesToUpdate(node, index, leftBound, rightBound):
    if (node.leftChild is None) and (node.rightChild is None):
        return [node]
    

    midPoint = (leftBound + rightBound)//2

    if index < midPoint:
        relevantDescendants = findNodesToUpdate(node.leftChild, index, leftBound, midPoint)
    else:
        relevantDescendants = findNodesToUpdate(node.rightChild, index, midPoint, rightBound)
    return relevantDescendants + [node]
    

def buildTree(nums):
    
    if len(nums) == 1:
        return Node(nums[0])
    
    total = sum(nums)
    rootNode = Node(val = total)
    
    midIndex = len(nums)//2
    leftChildTree = buildTree(nums[0:midIndex])
    rightChildTree = buildTree(nums[midIndex:])

    rootNode.leftChild = leftChildTree
    rootNode.rightChild = rightChildTree

    return rootNode
    

# building tree is straightforward. 
#     
# to update tree, we must traverse down the tree and update the appopriate spots. 
#     thought: how do we find index i? 
#     we look at n. if i > n/2, we go right. otherwise, go left. 
#      

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

s = NumArray(nums)
print("before")
print(s)
s.update(10,42)
print("after")
print(s)

# # print(repr(repr(t)))
# # print(t)
# # print("calling...")
# ans = findNodesToUpdate(t, 16, 0, len(nums))
# print("ans.val:", [a.val for a in ans])
# t = buildTree(nums)
# for i in range(0, len(nums)-1):
#     ans = findNodesToUpdate(t, i, 0, len(nums))
#     try:
#         assert(ans[0].val == i)
#     except:
#         print(i, "didn't work.")
# print("nodes to update...")
# for n in ans:
#     print(n.val)