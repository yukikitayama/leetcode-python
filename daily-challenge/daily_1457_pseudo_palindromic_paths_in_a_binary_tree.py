"""
- Recursion function
- Function to check whether a sequence of integers is a palindrome
  - At most one digit has an odd frequency
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        ans = 0

        stack = [(root, 0)]

        while stack:
            node, path = stack.pop()

            if node:

                # XOR makes bit 1 if occurrence is odd for each value
                path = path ^ (1 << node.val)

                # If leaf
                if not node.left and not node.right:

                    # If we have at most 1 bit in mask, when we turn off the right significant bit
                    # there will be no 1 bit in mask (== 0)
                    if path & (path - 1) == 0:
                        ans += 1

                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))

        return ans

