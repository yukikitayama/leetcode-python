"""
- Make a graph
- DFS
- Make a hashmap
  - Key: node
  - Value: max depth
- Return a list of nodes which have min depth in the hashmap

- Topological sorting and BFS
"""


from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        neighbors = collections.defaultdict(set)
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                # popped neighbor is the only neighbor to leaf,
                # because len(neighbors[leaf]) == 1 is in leaves list
                # start: leaf, end: neighbor
                neighbor = neighbors[leaf].pop()

                # Remove leaf because it doesn't need to visit again
                # Cut out leaves of neighbor until it becomes a leaf
                # start neighbor, end: leaf
                neighbors[neighbor].remove(leaf)

                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

