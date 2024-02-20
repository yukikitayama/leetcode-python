"""
iterate to next when child is none
when there is child node
  store curr.next to temporary
  modify curr.next points to child head
  modify child tail next points to temporary
Need separate recursion function?
  if child
    recursion
  recursion returns tail node of the child list

Ans
  preorder traversal (root -> left -> right)
  child pointer is left of binary tree
  next pointer is right of binary tree
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        def preorder(prev, curr):
            """prev: root, curr: left"""

            # Terminal: when left child is missing, return root, so that we can go to right next
            if not curr:
                return prev

            # Root
            curr.prev = prev
            prev.next = curr

            temp = curr.next

            # Left
            tail = preorder(curr, curr.child)
            # Clean up child
            curr.child = None

            # Right
            return preorder(tail, temp)

        sentinel = Node(None, None, head, None)

        preorder(sentinel, head)

        # Clean up head prev connections to sentinel
        sentinel.next.prev = None

        return sentinel.next