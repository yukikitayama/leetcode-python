from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node):

            nonlocal ans

            if not node:
                return (0, 0)

            left_sum, left_num = dfs(node.left)
            right_sum, right_num = dfs(node.right)

            curr_sum = node.val + left_sum + right_sum
            curr_num = 1 + left_num + right_num
            curr_avg = curr_sum // curr_num

            if curr_avg == node.val:
                ans += 1

            return (curr_sum, curr_num)

        dfs(root)

        return ans

