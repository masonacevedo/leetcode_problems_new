from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        ans = "[Node:"
        ans += " "
        ans += str(self.val)
        if self.next is None:
            ans += ", next: None"
        else:
            ans += ", next: " + str(self.next.val)
        ans += "]"
        return ans
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head

        curNode = head
        while curNode.next:
            nextVal = curNode.next.val
            curVal = curNode.val
            if nextVal == curVal:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next

        return head



l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

s = Solution()
ans = s.deleteDuplicates(l1)
# print("ans:", ans.next)
while ans:
    print("ans:", ans)
    ans = ans.next