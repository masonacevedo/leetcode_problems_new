from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        n = 0
        while current is not None:
            n += 1
            current = current.next
        
        if n == 1:
            return None
        
        removeIndex = n//2
        current = head
        i = 0
        while i < removeIndex:
            i += 1
            prev = current
            current = current.next
        
        # print("middle node value:", current.val)
        # print("prev  node. value:", prev.val)
        prev.next = current.next
        return head
            
            

# l6 = ListNode(val=6)
# l2 = ListNode(val=2, next=l6)
# l1 = ListNode(val=1, next=l2)
# l7 = ListNode(val=7, next=l1)
# l4 = ListNode(val=4, next=l7)
# l3 = ListNode(val=3, next=l4)
# H = ListNode(val = 1, next=l3)

# l4 = ListNode(val = 4)
# l3 = ListNode(val = 3, next=l4)
# l2 = ListNode(val = 2, next=l3)
H = ListNode(val = 1)


s = Solution()

current = s.deleteMiddle(H)

print("printing new list...")
while current is not None:
    print(current.val)
    current = current.next