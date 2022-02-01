from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_successor_value(node):
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr.val

        def find_predecessor_value(node):
            curr = node.left
            while curr.right:
                curr = curr.right
            return curr.val

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If no left and right child, we can just delete the current node
            if not root.left and not root.right:
                root = None

            # If it has right child, current node needs to be replaced with its successor
            elif root.right:
                root.val = find_successor_value(root)
                # After replace, we still needs to go down to delete the node which we used to replace
                # so second argument of deleteNode() is not key, but root.val
                root.right = self.deleteNode(root.right, root.val)

            else:
                root.val = find_predecessor_value(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

