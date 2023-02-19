from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.right = left
        root.left = right

        return root


class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = collections.deque()
        queue.append(root)

        while queue:

            curr = queue.popleft()

            if not curr:
                continue

            curr.right, curr.left = curr.left, curr.right

            if curr.right:
                queue.append(curr.right)

            if curr.left:
                queue.append(curr.left)

        return root

