"""
hashmap
  k: horizontal index
  v: list of vals

BFS

each index - min horizontal index
  get 0 indexed
"""

from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Edge
        if not root:
            return []

        h_to_vals = collections.defaultdict(list)

        queue = collections.deque()
        queue.append((root, 0))
        min_h = float("inf")

        while queue:

            for _ in range(len(queue)):

                node, c = queue.popleft()

                min_h = min(min_h, c)

                h_to_vals[c].append(node.val)

                if node.left:
                    queue.append((node.left, c - 1))

                if node.right:
                    queue.append((node.right, c + 1))

        n = len(h_to_vals.keys())
        ans = [[] for _ in range(n)]
        for k, v in h_to_vals.items():
            ans_k = k - min_h
            ans[ans_k] = v

        return ans