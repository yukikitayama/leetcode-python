"""
Inorder to get ascending sorted list
Pick middle to make a current node
  left part is left subtree
  right part is right subtree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        values = []

        def inorder(node):
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)

        inorder(root)

        def recursion(values):

            if not values:
                return None

            mid = len(values) // 2
            print(values, mid)
            node = TreeNode(values[mid])
            node.left = recursion(values[:mid])
            node.right = recursion(values[mid + 1:])

            return node

        return recursion(values)


