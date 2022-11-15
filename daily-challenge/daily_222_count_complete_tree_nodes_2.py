from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.countNodes(root.left) + 1 + self.countNodes(root.right) if root else 0


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        d = self.compute_depth(root)

        if d == 0:
            return 1

        left = 1
        # -1?
        right = 2**d - 1

        while left <= right:

            pivot = left + (right - left) // 2

            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        return 2**d - 1 + left

    def compute_depth(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            d += 1
            node = node.left
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        left = 0
        right = 2**d - 1

        for _ in range(d):
            mid = left + (right - left) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1

        return node is not None

