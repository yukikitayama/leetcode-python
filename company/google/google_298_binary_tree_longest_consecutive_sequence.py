"""
- DFS
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(child: Optional[TreeNode], parent: Optional[TreeNode], length: int):
            nonlocal ans
            if not child:
                return

            if parent and parent.val == (child.val - 1):
                length += 1
            else:
                length = 1

            ans = max(ans, length)

            dfs(child.left, child, length)
            dfs(child.right, child, length)

        dfs(root, None, 0)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    print(Solution().longestConsecutive(root))
