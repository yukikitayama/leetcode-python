"""
Idea
- 3 facts about binary search tree
  - Inorder traversal of binary search tree is an array in ascending order
  - Predecessor is one step left and then right till you can
  - Successor is one step right and then left till you can
- 3 situations to delete
  - Key node is a leaf
  - Key node is not a leaf and has right child
  - Key node is not a leaf, has no right child, but has left child

Complexity
- Time is O(logn) because to search a node to delete, because of property of binary search tree,
  search space gets half in every step.
- Space is O(logn) for the recursion stack
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                # First replace with a new value
                root.val = self.successor(root)
                # Then delete the node which has the new value
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val







