from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = collections.deque()
        queue.append(root)
        queue.append(root)

        while queue:

            left = queue.popleft()
            right = queue.popleft()

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)

        return True

    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:

        def recursion(left, right):

            if not left and not right:
                return True

            if not left or not right:
                return False

            return left.val == right.val and recursion(left.left, right.right) and recursion(left.right, right.left)

        return recursion(root, root)