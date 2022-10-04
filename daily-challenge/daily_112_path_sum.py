from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def recursion(node, curr):

            if not node:
                return False

            curr += node.val

            # If leaf
            if not node.left and not node.right:
                return curr == targetSum

            else:
                left_result = recursion(node.left, curr)
                right_result = recursion(node.right, curr)
                return left_result or right_result

        return recursion(root, 0)


if __name__ == '__main__':
    pass
