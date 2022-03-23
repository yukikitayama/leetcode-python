"""
- Do two traversals
- First, copy nodes
- Second, connect nodes
"""


from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        if not root:
            return None

        copy = {}

        # Copy nodes
        stack = [root]
        while stack:

            curr = stack.pop()

            copy[curr] = NodeCopy(curr.val)

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        # Connect nodes
        stack = [root]
        while stack:

            curr = stack.pop()

            if curr.left:
                copy[curr].left = copy[curr.left]
                stack.append(curr.left)
            if curr.right:
                copy[curr].right = copy[curr.right]
                stack.append(curr.right)
            if curr.random:
                copy[curr].random = copy[curr.random]

        return copy[root]
