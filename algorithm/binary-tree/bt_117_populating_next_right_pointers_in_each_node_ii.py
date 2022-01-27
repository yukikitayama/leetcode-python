"""
- Use constant space, but recursion stack is fine

- Establish next pointers for a level N while it's on level N - 1
- Think each level in binary tree as linked list
  - leftmost node is the head of each linked list
"""


import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def process_child(node, prev, leftmost):
            if node:
                if prev:
                    prev.next = node
                else:
                    leftmost = node

                prev = node
            return prev, leftmost

        leftmost = root

        while leftmost:

            prev = None
            curr = leftmost

            leftmost = None

            while curr:

                prev, leftmost = process_child(curr.left, prev, leftmost)
                prev, leftmost = process_child(curr.right, prev, leftmost)

                curr = curr.next

        return root


class Solution1:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        queue = collections.deque([root, None])

        while queue:

            curr = queue.popleft()

            if curr:
                curr.next = queue[0]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            else:
                if queue:
                    queue.append(None)

        return root


