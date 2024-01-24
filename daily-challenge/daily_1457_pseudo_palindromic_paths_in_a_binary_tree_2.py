"""
Pseudo-palindromic
  Every number needs to be even [1, 1, 2, 2]
  Every number even except one number [1, 1, 2, 2, 3]

Odd count needs to be 0 or 1 appearance

DFS
  collect current value in recursion
    hashmap?
    array?
      [0, 0, 1, 2]
      [0, 1, 1, 1]
  At leaf, check if the collected values are pseudo-palindromic
    iterate hashmap?

1 frequency at the 1st bit
2 frequency at the 2nd bit

XOR
  1 if odd
  0 if no appearance or even

At most one bit is set to 1.
"""

from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node, path):
            nonlocal ans

            path ^= (1 << node.val)

            if not node.left and not node.right:
                if path & (path - 1) == 0:
                    ans += 1
                return

            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root, 0)

        return ans


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(1)
    # 1

    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(1)
    # 2

    print(Solution().pseudoPalindromicPaths(root))




