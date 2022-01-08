from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_same(p, q):
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

            if not is_same(curr_p, curr_q):
                return False

            if curr_q:
                queue.append((curr_p.left, curr_q.left))
                queue.append((curr_p.right, curr_q.right))

        return True


if __name__ == '__main__':
    # p = TreeNode(1, TreeNode(2), TreeNode(3))
    # q = TreeNode(1, TreeNode(2), TreeNode(3))
    p = TreeNode(10)
    p.left = TreeNode(5)
    p.right = TreeNode(15)
    q = TreeNode(10)
    q.left = TreeNode(5)
    q.left.right = TreeNode(15)
    # False
    print(Solution().isSameTree(p, q))
