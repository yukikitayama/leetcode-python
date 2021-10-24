from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Take O(depth) to find depth
        d = self.compute_depth(root)
        if d == 0:
            return 1

        # Left is 1 because the last level is guaranteed to have at one node at the left
        left = 1
        right = 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2**d - 1) + left

    def compute_depth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    # Return True if the idx exists in the last level
    def exists(self, idx, d, node):
        left = 0
        right = 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None


