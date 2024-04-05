from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        # Edge
        if not root:
            return root

        first = None
        prev = None

        def inorder(node):
            nonlocal first, prev

            if node:

                inorder(node.left)

                if not first:
                    first = node

                if prev:
                    prev.right = node
                    node.left = prev

                prev = node

                inorder(node.right)

        inorder(root)

        first.left = prev
        prev.right = first

        return first
