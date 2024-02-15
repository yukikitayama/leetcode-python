"""
Create graph from give root
BFS to find the furthest node
From the found furthest node to run BFS again to find the furthest distance

Can I create graph?
  curr node
  for each child in its children
    create bidirectional graph

twice BFS approach doesn't work for this problem, not because of BFS, but because the trees in this problem
can contain duplicated numbers.

eg1
  6
    3
      1
        2
        4
    5
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        ans = 0

        def compute_height(node):
            nonlocal ans

            # Terminal: leaf
            if not node.children:
                return 0

            first_max_height = 0
            second_max_height = 0

            for child in node.children:

                # +1 is the edge between current node and current children
                curr_height = compute_height(child) + 1

                if curr_height > first_max_height:
                    second_max_height = first_max_height
                    first_max_height = curr_height

                elif curr_height > second_max_height:
                    second_max_height = curr_height

            ans = max(ans, first_max_height + second_max_height)

            return first_max_height

        compute_height(root)

        return ans
