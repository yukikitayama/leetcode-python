from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        head = None
        tail = None

        def inorder(node):
            nonlocal head, tail

            if node:
                inorder(node.left)

                # Only smallest val node
                if not head:
                    head = node

                if tail:
                    tail.right = node
                    node.left = tail

                tail = node

                inorder(node.right)

        inorder(root)

        head.left = tail
        tail.right = head

        return head