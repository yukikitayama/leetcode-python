from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Edge
        if not root:
            return root

        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:

            curr = []

            for _ in range(len(queue)):

                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(curr)

        return ans
