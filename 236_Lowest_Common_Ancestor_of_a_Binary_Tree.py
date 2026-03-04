from copy import deepcopy
from copy import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)

# dumb solution:
#   search down left tree and right tree.
#   if p and q are in left and right, LcA is root.
#   if both in left or both in right, LCA is lower. 
#   We cannot tell immediately from our perspective where p and q might be. 
#   I think we just have to search the whole tree... 
#   
#  Thought: We traverse the tree once, build a list of everyone's parents.
#    Then, we look at the first common parent of p and q. 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentMap = {}
        parentList = []

        traverse(root, parentMap, parentList)
        return lastCommonEntry(parentMap[p.val], parentMap[q.val])
    

def lastCommonEntry(l1, l2):
    for i in reversed(range(0, len(l1))):
        a = l1[i]
        for j in reversed(range(0, len(l2))):
            b = l2[j]
            if a == b:
                return a
    return None


def traverse(root, parentMap, parentList):
    if root is None:
        return
    
    parentMap[root.val] = parentList
    parentList.append(root)
    traverse(root.left, parentMap, copy(parentList))
    traverse(root.right, parentMap, copy(parentList))
        
l1 = TreeNode(6)

l3 = TreeNode(0)
l4 = TreeNode(8)

d1 = TreeNode(7)
d2 = TreeNode(4)

l2 = TreeNode(2, d1, d2)

m1 = TreeNode(5, l1, l2)
m2 = TreeNode(1, l3, l4)

r = TreeNode(3, m1, m2)

mySol = Solution()

ans = mySol.lowestCommonAncestor(r, d1, l3)
print("ans:", ans)
# for k,v in ans.items():
#     print(k, "|", v)