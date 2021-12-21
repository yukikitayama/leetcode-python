from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # Edge case
        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:

            depth += 1

            for _ in range(len(queue)):
                curr = queue.popleft()

                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().minDepth(root))
