"""
DFS
  return 1 if p or q
  set answer node if children sum is 2 or sum of child and current is 2
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def dfs(node):
            nonlocal ans

            if node:

                left = dfs(node.left)
                right = dfs(node.right)

                # print(node.val, left, right)

                if (left + right == 2) and not ans:
                    ans = node

                elif (node == p or node == q) and left + right == 1 and not ans:
                    ans = node

                return left + right + (node == p or node == q)

            else:
                return 0

        dfs(root)

        return ans
