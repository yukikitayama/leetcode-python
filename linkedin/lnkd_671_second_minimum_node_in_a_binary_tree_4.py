"""
  2
 / \
2   4
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        min_first = root.val

        def dfs(node):

            nonlocal ans

            if node:
                # Stop recursion when it finds the next smallest value
                # because all the values below current node have the value at least
                # current node.val, no need to search further
                # But it should search the current level other node values
                if min_first < node.val < ans:
                    ans = node.val

                # When min_first is equal to node.val, it comes here
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)

        return ans if ans != float('inf') else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# root = TreeNode(2)
# root.left = TreeNode(2)
# root.right = TreeNode(2)

print(Solution().findSecondMinimumValue(root))







