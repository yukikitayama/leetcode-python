"""
collect node values by hashmap
  horizontal index to list of node values

BFS and track depth and horizontal index
  depth for order in list in list
  index for indexing of a list

7:19
"""

from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        loc_to_values = collections.defaultdict(list)

        queue = collections.deque()
        # (node, horizontal location index)
        queue.append((root, 0))

        while queue:

            for _ in range(len(queue)):

                curr_node, loc = queue.popleft()
                curr_val = curr_node.val

                loc_to_values[loc].append(curr_val)

                if curr_node.left:
                    queue.append((curr_node.left, loc - 1))
                if curr_node.right:
                    queue.append((curr_node.right, loc + 1))

        # print(loc_to_values)

        # Wanna convert [-2, -1, 0, 1, 2] to [0, 1, 2, 3, 4]
        # -2 - (-2) = 0
        # -1 - (-2) = 1
        # 0 - (-2) = 2
        # 1 - (-2) = 3
        # [0, 1, 2, 3], min: 0
        # 0 - 0 = 0
        # 1 - 0 = 1

        min_horizontal_index = min(loc_to_values.keys())
        horizontal_length = len(loc_to_values.keys())
        ans = [None] * horizontal_length
        for k, v in loc_to_values.items():
            i = k - min_horizontal_index
            ans[i] = v

        return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    print(Solution().verticalOrder(root))
