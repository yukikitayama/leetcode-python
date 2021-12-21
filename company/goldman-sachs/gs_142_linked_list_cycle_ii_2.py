"""
- Floyd's hare and tortoise
"""


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        intersect = self.get_intersect(head)
        if not intersect:
            return None

        p1 = head
        p2 = intersect
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

    def get_intersect(self, head):
        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            # Found intersection
            if tortoise == hare:
                return tortoise

        # There's no cycle
        return None


"""
- Time is O(n), because it visits each node exactly once
- Space is O(n) for visited hash set.
"""
