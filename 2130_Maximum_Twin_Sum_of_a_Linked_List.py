from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# l6 = ListNode(val=6)
l2 = ListNode(val=2)
l1 = ListNode(val=1, next=l2)
l7 = ListNode(val=7, next=l1)
l4 = ListNode(val=4, next=l7)
l3 = ListNode(val=3, next=l4)
H = ListNode(val = 1, next=l3)

s = Solution()

ans = s.pairSum(H)
print("ans:", ans)