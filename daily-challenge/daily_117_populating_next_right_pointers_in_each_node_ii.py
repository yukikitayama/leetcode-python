"""
- BFS
- morris?

- To save space
- When we go to the level n, the next pointers at level n is already established,
  because when we are at level n - 1, we establish connection for level n
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
                # If this node is the first node in the next level
                else:
                    leftmost = node

                # Update prev to current node to iterate
                prev = node

            return prev, leftmost

        leftmost = root

        while leftmost:

            prev = None
            curr = leftmost

            # It will be updated or used as terminating while loop
            leftmost = None

            while curr:

                prev, leftmost = process_child(curr.left, prev, leftmost)
                prev, leftmost = process_child(curr.right, prev, leftmost)

                # Iterate current level
                curr = curr.next

        return root


class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:

            n = len(queue)

            for i in range(n):

                curr = queue.popleft()

                if i < n - 1:
                    curr.next = queue[0]

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return root
