# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
Hashmap
  k: original node
  v: copy node

DFS
  check all the neighbors of original
    refer copy node by hashmap
    append a new neighbor node to the copy node neighbors
  Recursion visit the next neighbor if not visited
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        copy = Node(node.val, [])
        original_to_copy = {node: copy}
        visited = set()

        def recursion(original):
            copy_node = original_to_copy[original]
            for neighbor in original.neighbors:
                if neighbor not in original_to_copy:
                    copy_neighbor = Node(neighbor.val, [])
                    original_to_copy[neighbor] = copy_neighbor

                copy_node.neighbors.append(original_to_copy[neighbor])

                if neighbor not in visited:
                    visited.add(neighbor)
                    recursion(neighbor)

        visited.add(node)
        recursion(node)

        return copy