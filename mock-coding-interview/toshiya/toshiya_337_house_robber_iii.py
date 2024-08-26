"""
func returns (money, boolean)
if rob, return (X, True)
if not rob, return (0, False)

Max so far

  3 + (1 + 3) + 3 = 7
  or
  4 + 5 = 9

At current number
  I need to know
    max so far from child
    or max so far from grand child with me
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def recursion(node) -> [int, int]:
            if node:

                left_child, left_grand = recursion(node.left)
                right_child, right_grand = recursion(node.right)

                take = node.val + left_grand + right_grand
                not_take = max(left_child, left_grand) + max(right_child, right_grand)

                # print(node.val, take, not_take)

                return [take, not_take]

            else:
                return [0, 0]

        return max(recursion(root))