"""
DFS to find height
Create matrix
BFS to fill the matrix
  row: height
  col: compute by parent and formula


c - 2 ** (height - r - 1)
c + 2 ** (height - r - 1)

c: 3, r: 0, height: 2
3 - 2 ** (2 - 0 - 1) = 3 - 2 = 1
3 + 2 ** (2 - 0 - 1) = 3 + 2 = 5
"""

from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = 0

        def dfs(node, h):
            nonlocal height

            # Leaf
            if not node.left and not node.right:
                height = max(height, h)
                return

            if node.left:
                dfs(node.left, h + 1)
            if node.right:
                dfs(node.right, h + 1)

        dfs(root, 0)

        # print(f"height: {height}")

        ans = [[""] * (2 ** (height + 1) - 1) for _ in range(height + 1)]

        # for row in ans:
        #     print(row)

        queue = collections.deque()
        c = (len(ans[0]) - 1) // 2
        queue.append((root, 0, c))

        while queue:

            for _ in range(len(queue)):

                node, r, c = queue.popleft()

                ans[r][c] = str(node.val)

                if node.left:
                    next_c = c - 2 ** (height - r - 1)
                    queue.append((node.left, r + 1, next_c))
                if node.right:
                    next_c = c + 2 ** (height - r - 1)
                    queue.append((node.right, r + 1, next_c))

        return ans
