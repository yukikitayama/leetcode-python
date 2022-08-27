"""
- Recursive function returns subtree path length and sum up
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def recursion(node) -> List[int]:
            nonlocal ans

            if not node:
                return [0, 0]

            inr = dcr = 1

            if node.left:
                left = recursion(node.left)
                if node.val == node.left.val + 1:
                    dcr = left[1] + 1
                elif node.val == node.left.val - 1:
                    inr = left[0] + 1

            if node.right:
                right = recursion(node.right)
                if node.val == node.right.val + 1:
                    dcr = max(dcr, right[1] + 1)
                elif node.val == node.right.val - 1:
                    inr = max(inr, right[0] + 1)

            # Subtract 1 so that current node is not counted twice
            ans = max(ans, dcr + inr - 1)
            return [inr, dcr]

        recursion(root)
        return ans

