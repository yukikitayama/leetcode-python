from typing import List, Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        # Edge
        if not root:
            return ans

        queue = collections.deque()
        queue.append(root)
        level = 0

        while queue:

            curr_array = []

            for _ in range(len(queue)):

                node = queue.popleft()

                curr_array.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 != 0:
                curr_array.reverse()

            ans.append(curr_array[:])

            level += 1

        return ans
