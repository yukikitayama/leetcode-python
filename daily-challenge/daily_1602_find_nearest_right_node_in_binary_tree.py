"""
- BFS
-
"""


from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return root

        queue = collections.deque([root, None])

        while queue:

            curr = queue.popleft()

            if curr == u:
                return queue.popleft()

            if curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # If curr is None
            else:
                if queue:
                    queue.append(None)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    u = root.left.right

    root = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    u = root.right.left

    ans = Solution().findNearestRightNode(root, u)
    print(ans.val) if ans else print(None)