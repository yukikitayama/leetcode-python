"""
- Not Rabbit and turtle algorithm
"""


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This set contains reference to linked list node
        visited = set()

        node = head

        # While loop stops when it reached the end of the linked list
        # because the end node does have next: None
        while node:
            if node in visited:
                return node

            else:
                visited.add(node)
                node = node.next

        return None


"""
- Time is O(n), because it visits each node exactly once
- Space is O(n) for visited hash set.
"""
