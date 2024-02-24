"""
Recursion
  from bottom, first node which collects 2 points is the LCA
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # ans = None

        # def recursion(node):
        #     nonlocal ans

        #     # If leaf
        #     if not node.left and not node.right:
        #         if node == p or node == q:
        #             return 1
        #         else:
        #             return 0

        #     left = 0
        #     if node.left:
        #         left = recursion(node.left)

        #     right = 0
        #     if node.right:
        #         right = recursion(node.right)

        #     if node == p or node == q:
        #         curr = 1
        #     else:
        #         curr = 0

        #     if left + curr + right == 2:
        #         if not ans:
        #             ans = node

        #     return left + curr + right

        # recursion(root)

        # return ans

        ans = None

        def recursion(node):
            nonlocal ans

            if not node:
                return 0

            left = recursion(node.left)
            right = recursion(node.right)
            curr = 0
            if node == p or node == q:
                curr = 1
            if left + curr + right == 2:
                ans = node

            return max(left, curr, right)

        recursion(root)

        return ans
