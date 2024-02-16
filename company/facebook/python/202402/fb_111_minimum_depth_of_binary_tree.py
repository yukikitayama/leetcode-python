"""
Depth in this problem is not the depth of the tree, but the number of nodes in the shortest path from node, including node

BFS
  when leaf node is found, return answer
  queue append node and number of nodes
    answer is current number of nodes plus 1
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
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = collections.deque()
        queue.append((root, 1))

        while queue:

            for _ in range(len(queue)):

                curr, depth = queue.popleft()

                if not curr.left and not curr.right:
                    return depth

                if curr.left:
                    queue.append((curr.left, depth + 1))
                if curr.right:
                    queue.append((curr.right, depth + 1))