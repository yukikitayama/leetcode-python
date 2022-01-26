"""
- inorder
  - left -> root -> right
- postorder
  - left -> right -> root
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        value_to_index = {v: i for i, v in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root_node = TreeNode(val=root_val)

            split_index = value_to_index[root_val]

            # Top down recursion
            root_node.right = helper(split_index + 1, right)
            root_node.left = helper(left, split_index - 1)

            return root_node

        return helper(0, len(inorder) - 1)


