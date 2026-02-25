from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansAsInt = int(listToNum(l1)) + int(listToNum(l2))
        return buildList(ansAsInt)

def buildList(n):
    if n == 0:
        return ListNode(0)
    nStr = str(n)
    
    i = 0
    while i < len(nStr):
        if i == 0:
            prevNode = ListNode(int(nStr[i]))
        else:
            
            newNode = ListNode(int(nStr[i]))
            newNode.next = prevNode
            prevNode = newNode
        i += 1


    if len(nStr) == 1:
        return prevNode
    return newNode
    
        

def listToNum(l):
    ans_string = ""
    
    currentNode = l
    while currentNode:
        ans_string += str(currentNode.val)
        currentNode = currentNode.next

    return "".join(list(reversed(ans_string)))



l3 = ListNode(3)
l2 = ListNode(4, l3)
l1 = ListNode(2, l2)

x3 = ListNode(4)
x2 = ListNode(6, x3)
x1 = ListNode(5, x2)

mySol = Solution()
ans = mySol.addTwoNumbers(x1, l1)
print("ans:", ans.val)
print("ans:", ans.next.val)
print("ans:", ans.next.next.val)

mySol = Solution()
