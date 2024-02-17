"""
Maybe not it's from root

Case
  curr node to leaf
  one leaf to one node to another leaf

If adjacent values are different, no action

DFS
  postorder
  termination
    if leaf
      return value and length 0
  if child vaue and current value are the same
    count 1 edge
  Update answer max length
    sum edges from left and right
  return
    current value to parent,
    max of either left or right
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, parent_val):
            nonlocal ans

            # Terminate
            if not node:
                return 0

            left_count = dfs(node.left, node.val)
            right_count = dfs(node.right, node.val)

            ans = max(ans, left_count + right_count)

            if node.val == parent_val:
                return max(left_count, right_count) + 1
            else:
                return 0

        dfs(root, None)

        return ans

        # ans = 0

        # def dfs(node):
        #     nonlocal ans

        #     # Terminate
        #     if not node:
        #         return 0, None

        #     left_count, left_val = dfs(node.left)
        #     right_count, right_val = dfs(node.right)

        #     if node.val == left_val and node.val == right_val:
        #         ans = max(ans, left_count + right_count)
        #     elif node.val == left_val:
        #         ans = max(ans, left_count)
        #     elif node.val == right_val:
        #         ans = max(ans, right_count)
        #     ans = max(ans, right_count)

        #     return max(left_count, right_count) + 1, node.val

        # dfs(root)

        # return ans
