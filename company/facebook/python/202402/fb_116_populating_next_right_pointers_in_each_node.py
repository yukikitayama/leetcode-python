"""
BFS
  when current element in the queue is last, do nothing
  otherwise current node next points at the leftmost node in the queue
"""

from typing import Optional
import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:

            n = len(queue)

            for i in range(n):

                node = queue.popleft()

                if i != n - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root



