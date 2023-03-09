from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        def get_intersect(node):
            tortoise = node
            hare = node

            while hare and hare.next:
                tortoise = tortoise.next
                hare = hare.next.next

                if tortoise == hare:
                    return tortoise

            return None

        intersect = get_intersect(head)

        if not intersect:
            return None

        p1 = head
        p2 = intersect

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()

        curr = head

        while curr:
            if curr in visited:
                return curr

            visited.add(curr)
            curr = curr.next

        return None


