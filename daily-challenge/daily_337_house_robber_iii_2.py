from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]):
        rob_saved = {}
        not_rob_saved = {}

        def helper(node, parent_robbed):
            if not node:
                return 0

            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                # Because parent was robbed, we cannot rob the current node
                # so the summation does not have node.val
                # Pass False to helper functions, because we don't rob the current node, which will be
                # a parent of the helper functions
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result

            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                # If parent was not robbed, we have two options
                # 1. rob the current node, or 2. not rob the current node again.
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result

        return helper(root, False)


