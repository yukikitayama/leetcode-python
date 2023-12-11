"""
Do level order traversal by BFS and reverse
"""

from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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

        ans.reverse()

        return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrderBottom(root))
