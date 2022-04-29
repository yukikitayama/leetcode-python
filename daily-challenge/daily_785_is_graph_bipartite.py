"""
- Bipartite graph is about edges
- Edge connects a node in one set to a node in the other set
- There is no edge which connect a node in one set to a node in the same set
- We should be able to greedily color the graph if and only if it's bipartite
- One node colored blue implies that all the neighbors are red
"""


from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # {node_index: 0 or 1}
        node_idx_to_color = {}

        for node in range(len(graph)):

            if node not in node_idx_to_color:

                stack = [node]

                # By default always starts coloring with 0
                # and neighbors will be 1
                node_idx_to_color[node] = 0

                while stack:

                    curr = stack.pop()

                    for neighbor in graph[curr]:

                        # If a neighbor is not colored yet
                        if neighbor not in node_idx_to_color:

                            # Color the neighbor with the different color from the current
                            # ^1 because color is binary
                            node_idx_to_color[neighbor] = node_idx_to_color[curr] ^ 1

                            # For next iteration
                            stack.append(neighbor)

                        # If we cannot form bipartite graph, return False
                        elif node_idx_to_color[neighbor] == node_idx_to_color[curr]:
                            return False

        return True


if __name__ == '__main__':
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    # False
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    # True
    print(Solution().isBipartite(graph))
