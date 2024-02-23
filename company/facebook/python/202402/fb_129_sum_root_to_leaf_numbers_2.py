"""
BFS
"""

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        queue = collections.deque()
        # (node, current number)
        queue.append((root, 0))

        while queue:

            for _ in range(len(queue)):

                node, curr = queue.popleft()

                curr = curr * 10 + node.val

                # If leaf
                if not node.left and not node.right:
                    ans += curr

                if node.left:
                    queue.append((node.left, curr))
                if node.right:
                    queue.append((node.right, curr))

        return ans
