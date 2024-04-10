"""
Recursion
  first node which collect 2 information is the LCA node
  Recursion return 0 if not p or q, 1 if p or q
  if current node receive 1 and current node is p or q,
    current node is LCA
  if current node receive True from both children,
    current node is LCA
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def recursion(node):
            nonlocal ans

            if node:

                left = recursion(node.left)
                right = recursion(node.right)

                if left + right == 2:
                    ans = node
                elif left + right == 1 and (node == p or node == q):
                    ans = node

                if node == p or node == q:
                    return 1
                else:
                    return max(left, right)

            # Child of leaf
            else:
                return 0

        recursion(root)

        return ans