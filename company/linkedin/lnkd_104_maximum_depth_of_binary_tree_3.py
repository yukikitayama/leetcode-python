from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        if root:
            queue.append((1, root))
        depth = 0

        while queue:

            n = len(queue)

            for _ in range(n):

                curr_depth, curr_node = queue.popleft()

                # print(f'curr_depth: {curr_depth}')

                if curr_node:
                    depth = max(depth, curr_depth)
                    queue.append((curr_depth + 1, curr_node.left))
                    queue.append((curr_depth + 1, curr_node.right))

        return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxDepth(root))
