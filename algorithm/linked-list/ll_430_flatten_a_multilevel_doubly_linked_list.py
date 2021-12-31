"""
- Preorder traversal
  - root, left, right
"""


from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        def recursion(prev, curr):

            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            next = curr.next

            # If curr.child exists, recursion eventually returns tail
            # If curr.child does not exist, returns curr
            tail_or_curr = recursion(curr, curr.child)

            # Need to reset child to be flatten
            curr.child = None

            return recursion(tail_or_curr, next)

        sentinel_node = Node(None, None, head, None)
        recursion(sentinel_node, head)

        # Unlink sentinel node
        sentinel_node.next.prev = None

        return sentinel_node.next




