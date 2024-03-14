"""
Hashmap
  k: val
  v: node

Each node has depth (distance between root and this node) and height (distance between this node and leaf)
Tree height is max(depth + height)
"""

from typing import Optional, List
import collections
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_val_to_d_and_h = collections.defaultdict(list)

        def recursion(node, depth):

            if not node:
                return -1

            else:
                node_val_to_d_and_h[node.val].append(depth)

                left_height = recursion(node.left, depth + 1)
                right_height = recursion(node.right, depth + 1)
                height = max(left_height, right_height) + 1

                node_val_to_d_and_h[node.val].append(height)

                return height

        recursion(root, 0)

        # print("node_val_to_d_and_h: ", node_val_to_d_and_h)

        depth_to_min_heap = {}

        for node_val, d_and_h in node_val_to_d_and_h.items():

            d, h = d_and_h

            if d not in depth_to_min_heap:
                min_heap = []
                heapq.heapify(min_heap)
                heapq.heappush(min_heap, (h, node_val))
                depth_to_min_heap[d] = min_heap

            else:
                min_heap = depth_to_min_heap[d]
                heapq.heappush(min_heap, (h, node_val))
                if len(min_heap) > 2:
                    heapq.heappop(min_heap)

        # print("depth_to_min_heap: ", depth_to_min_heap)

        # Queries
        ans = []

        for query in queries:

            depth, height = node_val_to_d_and_h[query]

            # At this depth, only one node exists, so by removing the height shrinks
            if len(depth_to_min_heap[depth]) == 1:
                ans.append(depth - 1)

            # If this node has the max height at this depth
            # Heigth shrinks
            elif depth_to_min_heap[depth][1][1] == query:
                ans.append(depth_to_min_heap[depth][0][0] + depth)

            # If this node has 2nd max height or smaller height at this depth
            # Choose max height
            # Else because min_heap only contains 2 nodes, and this query node might not be in the heap
            else:
                ans.append(depth_to_min_heap[depth][1][0] + depth)

        return ans