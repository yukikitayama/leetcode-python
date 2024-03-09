"""
Finding should happen when current is parent
  otherwise cannot connect child and parent after deleting node
found node
  if left and right
    right will replace node
  if left only
    left will replace node
  if right only
    right will replace node

Edge
  when target is root node

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        def find_successor_val(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val

        def find_predecessor_val(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Found node to delete
        else:
            # Leaf
            if not root.left and not root.right:
                return None

            # Not leaf with right child, replace by successor
            elif root.right:
                successor_val = find_successor_val(root)
                # Update val, not replacing node with another node
                root.val = successor_val
                # Delete original successor node
                root.right = self.deleteNode(root.right, root.val)

            # Not leaf with left child, replace by predecessor
            else:
                predecessor_val = find_predecessor_val(root)
                # Update val, not replacing node with another node
                root.val = predecessor_val
                # Delete original predecessor node
                root.left = self.deleteNode(root.left, root.val)

        return root

    def deleteNode1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Edge
        if not root:
            return root

        def recursion(node, parent, is_left):

            # Key node is found
            if node.val == key:
                left = node.left
                right = node.right
                if left and right:
                    if is_left:
                        parent.left = right
                        right.left = left

                    # Right
                    pass

                elif left and not right:
                    if is_left:
                        parent.left = left

                    # Right
                    pass

                elif not left and right:
                    if is_left:
                        parent.left = right

                    # Right
                    pass

                # If current is leaf
                else:
                    if is_left:
                        parent.left = None

            elif node.val > key:
                if node.left:
                    recursion(node.left, node)
            elif node.val < key:
                if node.right:
                    recursion(node.right, node)

        if root.val == key:
            left = root.left
            right = root.right
            if left and right:
                root = right

        recursion(root, None)