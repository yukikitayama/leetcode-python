"""
- Make linked list to a ring
- Find the new tail and point the next to None, and break the ring
- Return the new head
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # There's nothing to rotate
        if not head:
            return None
        # There's only one node, so pointless to rotate
        if not head.next:
            return head

        # Make ring and get the length of linked list
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # 1 -> 2 -> 3 -> 4 -> 5, n: 5, k: 2, 4 -> 5 -> 1 -> 2 -> 3
        # new tail is 3, n - k - 1 = 5 - 2 - 1 = 2, number of iterations from head to the new tail
        # 1st iteration 1 -> 2, 2nd iteration 2 -> 3

        # Find new tail
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        # Find new head
        new_head = new_tail.next

        # Break the link to make it back to linked list
        new_tail.next = None

        return new_head




