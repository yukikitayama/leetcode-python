"""
- Max so far in recursion
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0

        def dfs(node, max_so_far):

            nonlocal ans

            if not node:
                return

            if node.val >= max_so_far:
                ans += 1

            if node.left:
                dfs(node.left, max(node.val, max_so_far))
            if node.right:
                dfs(node.right, max(node.val, max_so_far))

        dfs(root, float('-inf'))

        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(Solution().goodNodes(root))
