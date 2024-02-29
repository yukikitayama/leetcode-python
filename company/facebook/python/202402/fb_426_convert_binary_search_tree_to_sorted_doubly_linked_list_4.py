"""
initialize head and tail None
Inorder traversal
  if node
    recursive to left

    if not tail
        when reaching leftmost, set head

    if tail
        tail.right = node
        node.left = tail

    tail = node

    recursive to right

After traversal
  connect head and tail
"""

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

