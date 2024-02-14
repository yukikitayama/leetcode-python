"""
BFS
  root level is 0
  when level is odd reversed collected values to ans list
"""

from typing import List, Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        ans = []
        depth = 0

        while queue:

            curr = []

            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if depth % 2 != 0:
                curr.reverse()

            ans.append(curr)
            depth += 1

        return ans

