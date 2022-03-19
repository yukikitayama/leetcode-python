"""
- BFS to do level by level traversal to make sure we output lower nodes later
- BFS queue also store the column index to allow us to output lower column index node first
  - column index starts with 0, and left child is -1, and right child is +1
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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        column_index_to_value = collections.defaultdict(list)

        # Queue: [(TreeNode, column index)]
        queue = collections.deque([(root, 0)])

        while queue:

            node, column = queue.popleft()

            if node:

                column_index_to_value[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        # Lower column index first by sort and hashmap contains index by level by lever by BFS so lower row first
        return [column_index_to_value[x] for x in sorted(column_index_to_value.keys())]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().verticalOrder(root))
