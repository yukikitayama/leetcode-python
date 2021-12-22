"""
- In iteration, make prev and connect
- Two pointers
  - Slow pointer move by one node
  - Fast pointer move by two nodes
  - When fast reaches the end of the list, slow should be in the middle.

"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            # prev <- curr <- curr.next
            curr.next, prev, curr = prev, curr, curr.next

        first = head
        second = prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
