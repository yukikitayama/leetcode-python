from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        if not root:
            return ans

        queue = collections.deque()
        queue.append(root)

        while queue:

            max_so_far = float("-inf")

            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr.val > max_so_far:
                    max_so_far = curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(max_so_far)

        return ans
