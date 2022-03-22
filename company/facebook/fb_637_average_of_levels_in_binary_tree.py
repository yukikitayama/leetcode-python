"""
- BFS
"""


from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        queue = collections.deque([root])

        while queue:

            sum_ = 0
            count = 0

            for _ in range(len(queue)):

                curr = queue.popleft()

                sum_ += curr.val
                count += 1

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(sum_ / count)

        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().averageOfLevels(root))
