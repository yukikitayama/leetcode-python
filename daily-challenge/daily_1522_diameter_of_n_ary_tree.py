"""
- Make the n-ary tree a graph
- Find the longest distance by DFS

- Longest path in a tree can only happen
  - Between two leaves nodes
  - Between a leaf node and the root node

- Iterate all non-leaf nodes
  - Select the top two longest paths bridged by the non-leaf node
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else[]


class Solution:
    def diameter(self, root: 'Node') -> int:
        diameter = 0

        def height(node):
            nonlocal diameter
            # At the leaf level
            if len(node.children) == 0:
                return 0
            max_height_1, max_height_2 = 0, 0

            # Try all the children at the current node to find the top 2 longest paths
            for child in node.children:

                parent_height = height(child) + 1

                if parent_height > max_height_1:
                    # If we find a longer one, update the ranking
                    max_height_1, max_height_2 = parent_height, max_height_1

                elif parent_height > max_height_2:
                    # It does not affect No.1
                    max_height_2 = parent_height

            # Possible longest path is two longest paths combined by one bridge non-lead node
            distance = max_height_1 + max_height_2

            diameter = max(diameter, distance)

            return max_height_1

        height(root)
        return diameter





