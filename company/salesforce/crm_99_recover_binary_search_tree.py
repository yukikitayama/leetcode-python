"""
- Keep prev (parent) and flag about left or right
  - Compare curr (child) and prev depending on flag
- Postorder traversal
"""


from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = []
        x = y = prev = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # current node (root) needs to be bigger than prev,
            # but if not, need to swap
            if prev and root.val < prev.val:
                y = root
                if x is None:
                    x = prev
                else:
                    break
            prev = root
            root = root.right

        # Swap
        x.val, y.val = y.val, x.val


