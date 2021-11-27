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
        values = set()

        def dfs(node):
            if node:
                values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        min_first = root.val
        min_second = float('inf')
        for value in values:
            if min_first < value < min_second:
                min_second = value
        return min_second if min_second != float('inf') else -1




root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# root = TreeNode(2)
# root.left = TreeNode(2)
# root.right = TreeNode(2)

print(Solution().findSecondMinimumValue(root))







