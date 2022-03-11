from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge case: None
        if not head:
            return head
        # Edge case: It only has one node
        if not head.next:
            return head

        # Make it ring
        old_tail = head
        n = 1
        # Find the old tail node and count how many nodes
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        # Make ring
        old_tail.next = head

        # Break it somewhere after new tail and before new head
        new_tail = head
        # -1 otherwise it jumps to new head, not new tail
        for _ in range(n - (k % n) - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        # Return new head
        return new_head
