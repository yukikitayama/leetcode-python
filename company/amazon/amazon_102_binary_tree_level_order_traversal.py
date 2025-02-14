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
        ans = []

        if not root:
            return ans

        queue = collections.deque([root])

        while queue:

            curr_list = []

            for _ in range(len(queue)):

                curr_node = queue.popleft()

                curr_list.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            ans.append(curr_list)

        return ans
