"""
Maybe hashmap
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def recursion(node):
            nonlocal ans

            if node:

                # Leaf
                if not node.left and not node.right:
                    if node is p or node is q:
                        return 1
                    else:
                        return 0

                left = recursion(node.left)
                right = recursion(node.right)

                if left + right == 2 and ans is None:
                    ans = node

                if (node is p or node is q) and (left == 1 or right == 1) and ans is None:
                    ans = node

                return left + right + (1 if node is p or node is q else 0)

            else:
                return 0

        recursion(root)

        return ans
