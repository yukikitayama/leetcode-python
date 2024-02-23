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

        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:
            n = len(queue)

            for i in range(n):

                curr = queue.popleft()

                if i == n - 1:
                    ans.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return ans
