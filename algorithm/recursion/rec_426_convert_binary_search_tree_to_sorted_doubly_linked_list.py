"""
- Inorder traversal in BST
-
"""


from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:

        if not root:
            return root

        first = None
        last = None

        def recursion(node):
            nonlocal first, last
            if node:
                # Inorder
                recursion(node.left)

                if last:
                    # Link previous node (last) to current node (node)
                    last.right = node
                    node.left = last

                # Else block is for only the first iteration
                # to keep the first node
                else:
                    first = node
                last = node

                recursion(node.right)

        recursion(root)

        # Circular
        last.right = first
        first.left = last

        return first


if __name__ == '__main__':
    print(Solution())