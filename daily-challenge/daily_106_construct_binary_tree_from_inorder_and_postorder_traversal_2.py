"""
- inorder: left -> root -> right
- postorder: left -> right -> root
- Rear of postorder has root to start with
- Get left subtree and right subtree from inorder by indexing what we got from postorder
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        value_to_inorder_index = {v: i for i, v in enumerate(inorder)}

        def recursion(left, right):
            if left > right:
                return

            val = postorder.pop()
            node = TreeNode(val)

            inorder_index = value_to_inorder_index[val]
            # Recursion to right first, because postorder gives us first
            # the root of right subtree
            node.right = recursion(inorder_index + 1, right)
            node.left = recursion(left, inorder_index - 1)

            return node

        return recursion(0, len(inorder) - 1)

