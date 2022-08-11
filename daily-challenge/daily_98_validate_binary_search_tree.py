"""
- Keep upper and lower limits for each node while traversing
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recursion(node, left, right):

            if not node:
                return True

            if node.val <= left or right <= node.val:
                return False

            return recursion(node.left, left, node.val) and recursion(node.right, node.val, right)

        return recursion(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    pass

