"""
- keep head
- keep prev
- get tail as curr
- tail.next to be head
- update head to be the tail
- unlink prev.next
- repeat k times
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge case
        if not head:
            return None
        if not head.next:
            return head

        # Make a ring
        n = 1
        old_tail = head
        while old_tail.next:
             n += 1
             old_tail = old_tail.next
        old_tail.next = head

        # Find new tail and unlink the next
        # Find the new head to return
        new_tail = head
        i = 0
        while i < (n - k % n - 1):
            new_tail = new_tail.next
            i += 1
        new_head = new_tail.next
        new_tail.next = None

        return new_head



