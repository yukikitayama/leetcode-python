"""
- Recursively go to left until None
- If left is None, go to right
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal idx

            if idx == n:
                return None

            val = preorder[idx]

            if val < lower or val > upper:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()