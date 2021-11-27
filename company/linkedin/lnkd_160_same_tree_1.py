"""
- recursion
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is not None:
            return False

        if p is not None and q is None:
            return False

        if p is None and q is None:
            return True

        return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
        )


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

p = TreeNode(1, left=TreeNode(2), right=None)
q = TreeNode(1, left=None, right=TreeNode(2))

p = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
q = TreeNode(1, left=TreeNode(1), right=TreeNode(2))

print(Solution().isSameTree(p, q))