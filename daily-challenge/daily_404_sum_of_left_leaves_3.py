# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        ans = 0

        def recursion(node, is_left):
            nonlocal ans
            if node:

                if is_left and not node.left and not node.right:
                    ans += node.val

                recursion(node.left, True)
                recursion(node.right, False)

        recursion(root, False)

        return ans
