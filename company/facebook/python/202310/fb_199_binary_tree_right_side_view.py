"""
- BFS
- IF the last node in the current level by queue, add it to answer list
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        next_level = collections.deque([root])
        ans = []

        while next_level:

            curr_level = next_level
            next_level = collections.deque()

            while curr_level:

                curr_node = curr_level.popleft()

                if curr_node.left:
                    next_level.append(curr_node.left)
                if curr_node.right:
                    next_level.append(curr_node.right)

            # Here curr_level queue is empty,
            # so in memory curr_node object is the last node in the current level
            ans.append(curr_node.val)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(Solution().rightSideView(root))
