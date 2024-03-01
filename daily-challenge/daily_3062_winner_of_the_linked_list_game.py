"""
prev
curr

prev = prev.next.next
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:

        # Edge
        if not head:
            return head

        point_balance = 0

        prev = head
        curr = head.next

        while True:

            even = prev.val
            odd = curr.val

            if even < odd:
                point_balance += 1
            elif even > odd:
                point_balance -= 1

            if not curr.next:
                break
            else:
                prev = prev.next.next
                curr = curr.next.next

        if point_balance > 0:
            return "Odd"
        elif point_balance < 0:
            return "Even"
        else:
            return "Tie"
