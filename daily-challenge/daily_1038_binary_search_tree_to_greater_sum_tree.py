"""
Recursion
  right -> root -> left
  argument node, cumsum
  return cumsum
  T: O(N)
  S: O(height)

Inorder 2 passes
  Inorder to collect values to array
  Compute cumsum from right to left in the array
  Inorder to assign the cumsum
  T: O(2N)
  S: O(N)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def recursion(node, cumsum):

            if node:

                cumsum = recursion(node.right, cumsum)

                curr_val = node.val

                node.val += cumsum

                cumsum = recursion(node.left, cumsum + curr_val)

                return cumsum

            else:
                return cumsum

        recursion(root, 0)

        return root
