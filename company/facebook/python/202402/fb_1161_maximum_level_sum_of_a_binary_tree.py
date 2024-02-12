"""
Problem
  might have negative
  tree won't be none

Algo
  BFS
  hashmap
    k: level
    v: level sum
  return level with the max sum
  T: O(N)
  S: O(N)
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_to_sum = collections.defaultdict(int)

        queue = collections.deque()
        queue.append((root, 1))

        # ans = 0
        # max_sum = float("-inf")

        while queue:

            for _ in range(len(queue)):

                curr_node, curr_level = queue.popleft()

                level_to_sum[curr_level] += curr_node.val

                if curr_node.left:
                    queue.append((curr_node.left, curr_level + 1))
                if curr_node.right:
                    queue.append((curr_node.right, curr_level + 1))

                    #     if level_to_sum[curr_level] > max_sum:
        #         max_sum = level_to_sum[curr_level]
        #         ans = curr_level

        # return ans

        max_sum = max(level_to_sum.values())
        for k, v in level_to_sum.items():
            if level_to_sum[k] == max_sum:
                return k
