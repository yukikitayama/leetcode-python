"""
- When child is not None
  - Set aside curr next
  - curr next is child,
  - child prev is prev next
- When child and next is None
  - curr next is the set aside node
- Keep the set-aside node in stack
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        dummy = Node(None, None, head, None)
        prev = dummy
        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            # stack is LIFO
            # Append next fist, and then append child
            # so we connects node in child first,
            # and then come back nodes in next to connect
            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        dummy.next.prev = None
        return dummy.next




