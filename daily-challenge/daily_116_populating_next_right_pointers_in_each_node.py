"""
- Level order traversal
- Use queue store nodes in level order
"""


from typing import Optional
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> Optional[Node]:

        if not root:
            return root

        leftmost = root

        while leftmost.left:

            head = leftmost
            while head:

                # Same parent
                head.left.next = head.right

                # Different parent
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root


class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:

            n = len(queue)

            for i in range(n):

                curr = queue.popleft()

                if i != n - 1:
                    curr.next = queue[0]

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return root



