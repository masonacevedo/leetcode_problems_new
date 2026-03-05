from typing import Optional
from copy import deepcopy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# idea: calculate leftMost depth, calculate rightmost depth, return the minimum of those 2 depths? 
#       note: if a node only has 1 child, we just return the depth of that child.

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        # holy shit!! beautiful algorithm!! 
        strings = []
        Traverse(root, "", strings)
        sortedStrings = sorted(strings)
        lengthDict = {}

        for s in sortedStrings:
            if len(s) in lengthDict:
                lengthDict[len(s)].append(s)
            else:
                lengthDict[len(s)] = [s]
        
        bestSoFar = float('-inf')
        for k in lengthDict.keys():
            stringsOfLengthK = lengthDict[k]
            width = determineWidth(stringsOfLengthK)
            bestSoFar = max(bestSoFar, width)

        return bestSoFar


def determineWidth(strings):
    # print("strings:", strings)
    stringsAsNums = [int(s, 2) for s in strings]
    return (max(stringsAsNums) - min(stringsAsNums)+1)



def Traverse(root, s, strings):
    # if root is None:
    #     return
    if root.left and root.right:
        traverseLeft = s + "0"
        traverseRight = s + "1"

        strings.append(traverseLeft)
        strings.append(traverseRight)

        Traverse(root.left, traverseLeft, strings)
        Traverse(root.right, traverseRight, strings)

    elif root.left:
        traverseLeft = s + "0"
        strings.append(traverseLeft)
        Traverse(root.left, traverseLeft, strings)        
    
    elif root.right:
        traverseRight = s + "1"
        strings.append(traverseRight)
        Traverse(root.right, traverseRight, strings)
    else:
        return



# l1 = TreeNode(5)
# m1 = TreeNode(3, l1, None)
# m2 = TreeNode(2)
# r = TreeNode(1, m1, m2)

# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n5 = TreeNode(5, n6, None)
# n9 = TreeNode(9, n7, None)
# n3 = TreeNode(3, n5, None)
# n2 = TreeNode(2, None, n9)
# n1 = TreeNode(1, n3, n2) 

# n2 = TreeNode(2)
# n1 = TreeNode(1)



# n8 = TreeNode(8)
# n22 = TreeNode(-22, None, n8)
# n71 = TreeNode(71)
# n54 = TreeNode(-54, n71, n22)
# n48 = TreeNode(48, n54)
# n100right = TreeNode(-100)
# nMinus48 = TreeNode(-48, n100right, n48)

# n100left = TreeNode(-100)
# n34 = TreeNode(-34, None, n100left)
# n37 = TreeNode(37, n34, nMinus48)


n1 = TreeNode(1)
s = Solution()

ans = s.widthOfBinaryTree(n1)
print("ans:", ans)