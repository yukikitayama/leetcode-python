from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        stack = []
        i = 0

        while i < len(traversal):

            level = 0

            while i < len(traversal) and traversal[i] == "-":
                level += 1
                i += 1

            num = 0
            while i < len(traversal) and traversal[i].isdigit():
                num = num * 10 + int(traversal[i])
                i += 1

            # Hard to understand
            # Find parent node for the current node
            while len(stack) > level:
                stack.pop()

            node = TreeNode(num)

            # stack top is parent node for the current node
            # If a node has only one child, that child is guaranteed to be the left child
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node

            stack.append(node)

        # After iteration, stack contains the last path from root to leaf
        # So the first element is root
        return stack[0]
