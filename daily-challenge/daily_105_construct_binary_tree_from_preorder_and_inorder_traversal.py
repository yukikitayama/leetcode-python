"""
- use preorder to pick root, because preorder is root -> left -> right
- use inorder to divide it into left subtree and right subtree, because inorder is left -> root -> right
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0

        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        def array_to_tree(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        return array_to_tree(0, len(preorder) - 1)
