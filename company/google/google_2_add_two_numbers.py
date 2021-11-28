from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        p = l1
        q = l2
        curr = dummy_head
        carry = 0

        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            summed = carry + x + y
            carry = summed // 10
            # add only first digit
            curr.next = ListNode(summed % 10)
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        # Add 1, remaining 2nd digit
        if carry > 0:
            curr.next = ListNode(carry)

        return dummy_head.next