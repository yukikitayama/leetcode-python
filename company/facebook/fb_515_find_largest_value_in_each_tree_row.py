"""
- BFS
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        row = [root]

        # print(f'row: {row}')

        while any(row):
            ans.append(max(node.val for node in row))
            row = [child for node in row for child in [node.left, node.right] if child]
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    root = None
    print(Solution().largestValues(root))
