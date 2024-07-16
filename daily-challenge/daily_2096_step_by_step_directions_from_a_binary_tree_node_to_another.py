"""
Recursion
  If current node is start
    if left child, return L
    if right child, return R
  if current node is dest, return D
  if not either start or dest,
    if both children are not L, R, D, return ""
    otherwise return the same child value

In-place modify
  modify the binary tree to be bidirectional by adding parent
  first traversal
    make bidirectional
    save start node
  from start node, BFS until destination node
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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def find_start_node(node):
            if not node:
                return None

            if node.val == startValue:
                return node

            left = find_start_node(node.left)

            if left:
                return left

            right = find_start_node(node.right)

            return right

        parent_map = {}

        def populate_parent_map(node):
            if not node:
                return

            if node.left:
                parent_map[node.left.val] = node
                populate_parent_map(node.left)

            if node.right:
                parent_map[node.right.val] = node
                populate_parent_map(node.right)

        # k: next node, v: (curr node, path)
        path_tracker = {}

        def backtrack_path(node):
            path = []

            while node in path_tracker:
                prev, path_str = path_tracker[node]
                path.append(path_str)
                node = prev

            path.reverse()

            return "".join(path)

        # Find start node
        start_node = find_start_node(root)

        # print(start_node.val)

        # Populate parent hashmap, k: node value, v: parent node
        populate_parent_map(root)

        # print(parent_map)

        # BFS to find the path
        queue = collections.deque()
        queue.append(start_node)
        visited = set()
        visited.add(start_node)

        while queue:

            curr = queue.popleft()

            if curr.val == destValue:
                # return path string
                return backtrack_path(curr)

            # Check parent
            if curr.val in parent_map:
                parent = parent_map[curr.val]
                if parent not in visited:
                    queue.append(parent)
                    visited.add(parent)
                    # Add U because moving from curr to parent
                    path_tracker[parent] = (curr, "U")

            # Check left child
            if curr.left and curr.left not in visited:
                queue.append(curr.left)
                visited.add(curr.left)
                path_tracker[curr.left] = (curr, "L")

            # Check right child
            if curr.right and curr.right not in visited:
                queue.append(curr.right)
                visited.add(curr.right)
                path_tracker[curr.right] = (curr, "R")

        return ""