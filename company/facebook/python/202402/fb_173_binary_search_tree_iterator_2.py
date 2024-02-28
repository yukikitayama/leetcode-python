# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Next
  move pointer in BST, not in array
  stack
"""

from typing import Optional


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

        # If curr has right, append right, and append all the left

    def next(self) -> int:
        top = self.stack.pop()

        if top.right:
            curr = top.right
            while curr:
                self.stack.append(curr)
                curr = curr.left

        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class BSTIterator1:

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = -1
        self.array = []

        def inorder(node):
            if node:
                inorder(node.left)
                self.array.append(node.val)
                inorder(node.right)

        inorder(root)

    def next(self) -> int:
        self.pointer += 1
        return self.array[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.array) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()