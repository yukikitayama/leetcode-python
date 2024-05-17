from typing import List, Optional
import functools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

        # Base case
        for i in range(1, n + 1):
            dp[i][i] = [TreeNode(i)]

        #
        for number_of_nodes in range(2, n + 1):

            # n: 5, num: 2, n - num + 2 = 5 - 2 + 2 = 5, from 1 to 4
            for start in range(1, n - number_of_nodes + 2):

                # start: 1, num: 2, 1 + 2 - 1 = 2
                end = start + number_of_nodes - 1

                for i in range(start, end + 1):

                    left_subtrees = dp[start][i - 1] if i != start else [None]
                    right_subtrees = dp[i + 1][end] if i != end else [None]

                    for left in left_subtrees:
                        for right in right_subtrees:
                            root = TreeNode(i, left, right)
                            dp[start][end].append(root)

        return dp[1][n]

    def generateTrees1(self, n: int) -> List[Optional[TreeNode]]:

        @functools.cache
        def all_possible_bst(left, right):
            ans = []

            # Base case
            if left > right:
                ans.append(None)
                return ans

            for root in range(left, right + 1):

                left_subtrees = all_possible_bst(left, root - 1)
                right_subtrees = all_possible_bst(root + 1, right)

                # Brute force connecting left subtrees and right subtrees
                for left_node in left_subtrees:
                    for right_node in right_subtrees:
                        root_node = TreeNode(root, left_node, right_node)
                        ans.append(root_node)

            return ans

        return all_possible_bst(1, n)