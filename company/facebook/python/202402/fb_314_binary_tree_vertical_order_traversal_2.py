"""
BFS
  Order by the vertical can maintain by level order traversal and from left to right
  horizontal index can be decided by the root as 0
    -1 to left,
    1 to right
  hashmap
    k: horizontal
    v: list of vertically collected integers

Get minimum of key
  subtract the min from all the keys to adjust real array index
    eg. -2 -> -2 --2 = 0, 2 -> 2 - 2 -> 0
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

        if not root:
            return []

        loc_to_vals = collections.defaultdict(list)
        queue = collections.deque()
        # [(node, horizontal location)]
        queue.append((root, 0))

        while queue:

            for _ in range(len(queue)):

                node, loc = queue.popleft()

                loc_to_vals[loc].append(node.val)

                if node.left:
                    queue.append((node.left, loc - 1))
                if node.right:
                    queue.append((node.right, loc + 1))

        min_loc = min(loc_to_vals.keys())
        loc_length = len(loc_to_vals.keys())
        ans = [None] * loc_length
        for k, v in loc_to_vals.items():
            i = k - min_loc
            ans[i] = v

        return ans
