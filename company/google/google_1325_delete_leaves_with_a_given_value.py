from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        else:
            return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    target = 2
    ans = Solution().removeLeafNodes(root, target)
    print(ans.val)
    print(ans.left)
    print(ans.right.val)
    print(ans.right.left)
    print(ans.right.right.val)
