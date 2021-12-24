from typing import Optional
import collections


class Node:
    def __init__(self, val: int=0, left: 'Node'=None, right: 'Node'=None, next: 'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        queue = collections.deque()
        queue.append(root)

        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()

                if i == (n - 1):
                    curr.next = None
                else:
                    curr.next = queue[0]

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return root
