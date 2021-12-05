"""
- Distance between two nodes is the number of edges that connect the two nodes
- Height is the maximum distance between the root and all its leaf nodes
- In topological sorting, the vertex that has the least dependency appear first in the order
- In tree context, it means lead nodes appear first.
"""


from typing import List
import collections
import pprint


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        # Make an adjacency list
        neighbors = collections.defaultdict(set)
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # pprint.pprint(neighbors)

        # Initialize the first layer of leaves
        queue = collections.deque()
        for i in range(n):
            # If a current vertex connect only with 1 node,
            # the 1 node is the parent node, and the current vertex is a leaf
            if len(neighbors[i]) == 1:
                # Leaf does not have a chile, meaning no dependency in topological sorting
                # so first appended to queue
                queue.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(queue)
            new_leaves = collections.deque()

            while queue:
                """
                e.g.
                  1
                 /  \
                0    2
                neighbors: {1: {0, 2}, 0: {1}, 2: {1}},  
                queue: [0, 2]
                leaf: 0, neighbor: 1, neighbors:  {1: {0, 2}, 0: None, 2: {1}}
                neighbors[1].remove(0): neighbors: {1: {2}, 0: None, 2: {1}}
                """
                # By cutting out the leaves, it will find new leaves
                leaf = queue.popleft()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)

                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            queue = new_leaves

        return list(queue)


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
# [1]
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# [3, 4]
print(Solution().findMinHeightTrees(n, edges))
