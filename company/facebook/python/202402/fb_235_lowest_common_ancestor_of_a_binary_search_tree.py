# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recursion(node):
            if p.val < node.val and q.val < node.val:
                # Eventually node will be returned
                return recursion(node.left)
            elif p.val > node.val and q.val > node.val:
                # Eventually node will be returned
                return recursion(node.right)
            # 1. First split where left and right are in different child side
            # 2. First time to see p or q
            else:
                # This is the only return statement which returns node
                return node

        return recursion(root)
