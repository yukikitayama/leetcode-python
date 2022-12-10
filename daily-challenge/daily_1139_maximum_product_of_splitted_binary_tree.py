from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        sums = []

        def recursion(node):
            if not node:
                return 0

            sum_left = recursion(node.left)
            sum_right = recursion(node.right)
            sum_subtree = sum_left + node.val + sum_right

            sums.append(sum_subtree)

            return sum_subtree

        total = recursion(root)

        ans = float('-inf')

        for sum_ in sums:

            ans = max(ans, (total - sum_) * sum_)

        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    print(Solution().maxProduct(root))
