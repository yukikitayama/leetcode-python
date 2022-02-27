"""
- BFS?
- Assign index to each node to calculate width
  - index is parent index * 2 + 0 if left, index * 2 + 1 if right
  - * 2 is because binary tree doubles each level
"""


from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        if not root:
            return ans

        # Queue: [(node, index), ...]
        queue = collections.deque()
        queue.append((root, 0))

        while queue:

            for i in range(len(queue)):

                curr_node, curr_index = queue.popleft()

                if i == 0:
                    min_index = curr_index

                if curr_node.left:
                    queue.append((curr_node.left, curr_index * 2))

                if curr_node.right:
                    queue.append((curr_node.right, curr_index * 2 + 1))

            # At the end of for loop, curr_index is the max index,
            # + 1 because index is 0-based
            ans = max(ans, curr_index - min_index + 1)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    print(Solution().widthOfBinaryTree(root))
