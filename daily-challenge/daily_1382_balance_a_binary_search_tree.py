"""
Inorder to collect values to array
Recreate BST from the array
  Pick middle element as root from the current subarray
  left to before middle to be left child
  after middle to right to be right child
  preorder traversal
  return itself
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
                left = inorder(node.left)
                values.append(node.val)
                right = inorder(node.right)

        inorder(root)

        # print(values)

        def preorder(left, right):

            # Base case: Leaf
            if left == right:
                return TreeNode(values[left])

            # Base case: None as child of leaf
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(values[mid])

            left_node = preorder(left, mid - 1)
            right_node = preorder(mid + 1, right)

            node.left = left_node
            node.right = right_node

            return node

        ans = preorder(0, len(values) - 1)

        return ans