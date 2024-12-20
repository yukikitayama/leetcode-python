from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        queue = collections.deque()
        queue.append(root)
        level = 0

        while queue:

            current_level_nodes = []

            for _ in range(len(queue)):

                node = queue.popleft()
                current_level_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                # Swap
                left = 0
                right = len(current_level_nodes) - 1
                while left < right:
                    current_level_nodes[left].val, current_level_nodes[right].val = current_level_nodes[right].val, \
                    current_level_nodes[left].val
                    left += 1
                    right -= 1

            level += 1

        return root