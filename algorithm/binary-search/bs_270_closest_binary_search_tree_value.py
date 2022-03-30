from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        while root:
            ans = min(ans, root.val, key=lambda x: abs(target - x))
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return ans


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    target = 3.71
    print(Solution().closestValue(root, target))
