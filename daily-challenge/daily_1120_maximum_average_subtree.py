"""
recursive function returns sum of subtree values and count of trees in subtree
"""

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        ans = float("-inf")

        def recursion(node):
            """Output: (sum of value in this subtree, count of nodes in this subtree)"""

            nonlocal ans

            if not node:
                return 0, 0

            left_sum, left_count = recursion(node.left)
            right_sum, right_count = recursion(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            curr_ave = curr_sum / curr_count

            # print(f"curr_ave: {curr_ave}")

            ans = max(ans, curr_ave)

            return curr_sum, curr_count

        recursion(root)

        return ans


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(1)

    root = TreeNode(0)
    root.right = TreeNode(1)

    print(Solution().maximumAverageSubtree(root))
