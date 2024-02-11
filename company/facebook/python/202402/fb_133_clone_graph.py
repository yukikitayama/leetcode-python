# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
neighbors is a list of nodes, not vals

hashmap
  k: original node
  v: cloned node

BFS
  current original node
  create a new node

  save val and node to hashmap

  for each node in curr node neighbors
    if new node not in hashmap
      append to queue
    if new node in hashmap
      append the value to new node neighbors list
"""

from typing import Optional
import collections


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        visited = {}

        cloned_node = Node(node.val, [])
        visited[node] = cloned_node

        queue = collections.deque()
        queue.append(node)

        while queue:

            for _ in range(len(queue)):

                curr_node = queue.popleft()

                for neighbor_node in curr_node.neighbors:

                    if neighbor_node not in visited:
                        visited[neighbor_node] = Node(neighbor_node.val, [])

                        queue.append(neighbor_node)

                    visited[curr_node].neighbors.append(visited[neighbor_node])

        return visited[node]