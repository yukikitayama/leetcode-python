"""
- iteration
"""


from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_equal(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        queue = collections.deque([(p, q)])
        while queue:
            curr_p, curr_q = queue.popleft()

            if not is_equal(curr_p, curr_q):
                return False

            if curr_p:
                queue.append((curr_p.left, curr_q.left))
                queue.append((curr_p.right, curr_q.right))

        return True


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