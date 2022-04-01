"""
- Traverse all
- counter

- Inorder traversal of BST to get ascending order
- compare current with previous
  - if match, increment count
"""


from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        num_to_count = collections.defaultdict(int)

        def dfs(node):
            if node:
                num_to_count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        mode = max(num_to_count.values())

        return [k for k, v in num_to_count.items() if v == mode]


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    print(Solution().findMode(root))

