from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        queue = collections.deque([root])
        is_left = True

        ans = []

        while queue:

            curr_level = collections.deque()

            for _ in range(len(queue)):

                curr_node = queue.popleft()

                if is_left:
                    curr_level.append(curr_node.val)
                else:
                    curr_level.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            ans.append(curr_level)
            is_left = not is_left

        return ans



