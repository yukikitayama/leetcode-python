"""
DFS
  At leaf
    return current val, 1
  from left child
    receive sum and count
  from right child
    receive sum and count
  current cum = left sum + right cum + 1
  current count = left count + right count + 1
  compute average
    if the average is equal to current value, count up the answer integer

  return current sum and current count
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        if not root:
            return 0

        ans = 0

        def dfs(node):
            nonlocal ans

            if not node.left and not node.right:
                ans += 1
                return node.val, 1

            if node.left:
                left_sum, left_count = dfs(node.left)
            else:
                left_sum = 0
                left_count = 0

            if node.right:
                right_sum, right_count = dfs(node.right)
            else:
                right_sum = 0
                right_count = 0

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1

            if curr_sum // curr_count == node.val:
                ans += 1

            return curr_sum, curr_count

        dfs(root)

        return ans
