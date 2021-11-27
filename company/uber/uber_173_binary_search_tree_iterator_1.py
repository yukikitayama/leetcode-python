"""
- In binary search tree, inorder traversal gives us the nodes in non-decreasing order
  - Inorder is: left, root, right
  - Inorder traversal of binary search tree gives us the elements in a sorted order
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.buffer = []
        self.index = -1
        self._inorder(root)

    # Single leading underscore: Internal use indicator, not imported by from M import *
    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self.buffer.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        self.index += 1
        return self.buffer[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.buffer)


"""
Complexity
- Time
  - Constructor takes O(n)
  - next() and hasNext() takes O(1)
- Space
  - Let h be the height of the tree
  - Constructor takes recursion stack O(h)
  - O(n) for buffer array
"""

