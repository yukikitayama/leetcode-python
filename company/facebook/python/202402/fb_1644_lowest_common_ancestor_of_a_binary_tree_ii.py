"""
If p and q are not in the same path from root to leaf,
  Their lowest common parent is the answer
If p and q are in the same path
  Higher node is the answer
If either p or q doesn't exist in the tree,
  None is answer

From p or q, I wanna go up
  First node which meets conditions is the answer

Preorder

If p or q, return 1
  First node which gets 2 (include current node) is answer
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

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left + right == 2:
                ans = node
                return 1

            elif left + right == 1 and (node == p or node == q):
                ans = node
                return 1

            elif left + right == 1 and node != p and node != q:
                return 1

            elif node == p or node == q:
                return 1
            else:
                return 0

        dfs(root)

        return ans
