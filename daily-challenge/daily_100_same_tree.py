from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Successfully reach leaves
        if not p and not q:
            return True

        # Either reach leaf
        elif not p or not q:
            return False

        # Middle of tree, different value
        elif p.val != q.val:
            return False

        # Middle of tree, same value
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution:
    def isSameTree(self, p, q):

        def check(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            return True

        queue = collections.deque([(p, q)])

        while queue:

            p, q = queue.popleft()

            if not check(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True

