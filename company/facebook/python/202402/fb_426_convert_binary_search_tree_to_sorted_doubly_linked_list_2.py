"""
initialize head as none
Inorder traversal DFS to visit node in sorted order
  if leaf, return curr
    if head is none, set curr node, otherwise no update
  left
  root
    curr's prev is left
    curr's next is right
  right

  return curr as next prev

The recursion eventually outpus tail node
  set tail node and head
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
        prev = None

        def inorder(node):
            nonlocal head, prev

            if node:
                inorder(node.left)

                if prev:
                    prev.right = node
                    node.left = prev
                # Smallest case to set head
                else:
                    head = node

                prev = node

                inorder(node.right)

        inorder(root)
        # During recursion, head was updated once, tail was updated every time,
        # current value of tail is the last visited node, which is real tail
        prev.right = head
        head.left = prev

        return head