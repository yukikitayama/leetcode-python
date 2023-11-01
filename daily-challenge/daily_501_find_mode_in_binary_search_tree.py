from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        counter = collections.defaultdict(int)

        def dfs(node):
            if not node:
                return

            counter[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_freq = max(counter.values())

        ans = []
        for k, v in counter.items():
            if v == max_freq:
                ans.append(k)

        return ans


class SolutionInorderDFS:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        values = []

        def inorder_dfs(node: Optional[TreeNode]):

            if not node:
                return

            inorder_dfs(node.left)
            values.append(node.val)
            inorder_dfs(node.right)

        inorder_dfs(root)

        ans = []
        curr_num = float("-inf")
        curr_streak = 0
        max_streak = 0

        for num in values:

            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak

            if curr_streak == max_streak:
                ans.append(num)

        return ans




