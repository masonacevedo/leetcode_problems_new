from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, ceiling = float('inf'), floor = float('-inf'))

    def isValidBSTHelper(self, root: Optional[TreeNode], ceiling, floor) -> bool:
        if root is None:
            return True
        
        if root.val >= ceiling:
            return False
        
        if root.val <= floor:
            return False

        leftChild = root.left
        rightChild = root.right

        if leftChild:
            leftTreeValid = self.isValidBSTHelper(root.left, root.val, floor)
        else:
            leftTreeValid = True


        if rightChild:
            rightChildValid = self.isValidBSTHelper(root.right, ceiling, root.val)
        else:
            rightChildValid = True
        
        return leftTreeValid and rightChildValid

l1 = TreeNode(2)
l2 = TreeNode(2)

r = TreeNode(2, l1, l2)

s = Solution()
print("final ans:", s.isValidBST(r))