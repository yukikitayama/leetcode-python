"""
- Store diff between k and curr val in set
- Recursion
- If target is bigger than curr, go right, otherwise left
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        vals = inorder(root)

        # print(vals)

        l = 0
        r = len(vals) - 1

        while l < r:

            sum_ = vals[l] + vals[r]

            if sum_ == k:
                return True
            elif sum_ < k:
                l += 1
            else:
                r -= 1

        return False


class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def recursion(node, seen):

            if not node:
                return False

            if k - node.val in seen:
                return True

            seen.add(node.val)

            return recursion(node.left, seen) or recursion(node.right, seen)

        return recursion(root, set())


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    k = 9
    print(Solution().findTarget(root, k))
