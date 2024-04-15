from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def recursion(node, curr_num):
            nonlocal ans

            if node:

                curr_num = curr_num * 10 + node.val

                # Leaf
                if not node.left and not node.right:
                    ans += curr_num

                recursion(node.left, curr_num)
                recursion(node.right, curr_num)

        recursion(root, 0)

        return ans

    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def recursion(node, curr_num):
            nonlocal ans

            if node:

                # Leaf
                if not node.left and not node.right:
                    ans += curr_num * 10 + node.val

                recursion(node.left, curr_num * 10 + node.val)
                recursion(node.right, curr_num * 10 + node.val)

        recursion(root, 0)

        return ans
