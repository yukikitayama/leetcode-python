from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # not head works for empty linked list, and normal linked list tail termination
        # not head.next works for one length linkest list, which doesn't need to perform reverse
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)

        # Reverse happens here
        # if we have 1 -> 2 <- 3, and we (head) are at 1, we want 2's next to be 1
        head.next.next = head

        # Avoid cycle
        head.next = None

        # if head:
        #     print(p, head.val)

        # Always carry tail node for ans's head
        return p

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_ = curr.next
            curr.next = prev

            prev = curr
            curr = next_

        return prev