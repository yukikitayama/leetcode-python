"""
BFS to recover
save the values to hashset
find from hashset
"""

import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()

        queue = collections.deque([(root, 0)])
        while queue:

            for _ in range(len(queue)):
                curr, val = queue.popleft()
                curr.val = val
                self.values.add(val)
                if curr.left:
                    queue.append((curr.left, 2 * val + 1))
                if curr.right:
                    queue.append((curr.right, 2 * val + 2))

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)