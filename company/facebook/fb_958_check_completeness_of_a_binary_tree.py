"""
- First, compute height
- Second, BFS to check each level
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0

        # As soon as containing None, it stops
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1

        # print(f'i: {i}')
        # for node in bfs:
        #     if node:
        #         print(node.val)
        #     else:
        #         print(node)

        # If not complete tree, bfs[i:] will contain at least one True
        # so any() returns True, so solution returns False
        return not any(bfs[i:])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(Solution().isCompleteTree(root))
