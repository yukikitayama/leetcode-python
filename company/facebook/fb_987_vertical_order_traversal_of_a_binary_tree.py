"""
- BFS
- Hashmap
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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        # A list to hold the result of BFS,
        # but need to further sorting for requirement as answer
        # List: [(column index, row index, TreeNode value), (...), ...]
        # This order is sorting requirement
        node_list = []

        # BFS to assign column and row index to each node
        # Queue: [(TreeNode, row index, column index), (...), ...]
        queue = collections.deque([(root, 0, 0)])
        while queue:
            curr_node, row, column = queue.popleft()

            if curr_node:

                node_list.append((column, row, curr_node.val))

                # row + 1 because in BFS it does level by level traversal
                queue.append((curr_node.left, row + 1, column - 1))
                queue.append((curr_node.right, row + 1, column + 1))

        # Sort by indices and values to make left column first, higher row first, and smaller value first
        node_list.sort()

        # print(f'node_list: {node_list}')

        # Create an hashmap {column_index: a list of values}
        column_to_value = collections.OrderedDict()
        for col, row, val in node_list:
            if col not in column_to_value:
                column_to_value[col] = [val]
            else:
                column_to_value[col].append(val)

        # print(f'column_to_value: {column_to_value}')

        return list(column_to_value.values())


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(Solution().verticalTraversal(root))
