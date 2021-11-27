"""
- Max depth is current 1 plus the max of left depth and right depth
  - The single TreeNode has the depth 1

- Space is O(n) because
  - In worst case, tree is completely unbalanced, e.g. sequence of left children
  - Recursion call is stacked in call stack n times
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root = TreeNode(1)
root.right = TreeNode(2)

# root = None

# root = TreeNode(0)

print(Solution().maxDepth(root))


