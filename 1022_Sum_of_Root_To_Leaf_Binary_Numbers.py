from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        all_paths = self.sumRootToLeafHelper(root)
        ans = 0
        for p in all_paths:
            ans += int(p,2)
        return ans
    
    def sumRootToLeafHelper(self, root):
        # print("root.val:", root.val)        

        if (root.left is None) and (root.right is None):
            return [str(root.val)]

        all_paths = []
        if not(root.left is None):
            leftPathPossibilities = self.sumRootToLeafHelper(root.left)
            actualLeftPaths = [str(root.val) + p for p in leftPathPossibilities]
            all_paths += actualLeftPaths

        if not(root.right is None):
            rightPathPossibilities = self.sumRootToLeafHelper(root.right)
            actualRightPaths = [str(root.val) + p for p in rightPathPossibilities]
            all_paths += actualRightPaths

        return all_paths
        

mySol = Solution()

leaf1 = TreeNode(0)
leaf2 = TreeNode(1)
leaf3 = TreeNode(0)
leaf4 = TreeNode(1)

mid1 = TreeNode(0, leaf1, leaf2)
mid2 = TreeNode(1, leaf3, leaf4)

r = TreeNode(1, mid1, mid2)

ans_1 = mySol.sumRootToLeaf(r)

print("ans_1:", ans_1)
assert(ans_1 == 22)



leaf_2 = TreeNode(1)
root_2 = TreeNode(1, leaf_2, None)
ans_2 = mySol.sumRootToLeaf(root_2)
# assert(ans_2 == 3)
print("ans_2:", ans_2)