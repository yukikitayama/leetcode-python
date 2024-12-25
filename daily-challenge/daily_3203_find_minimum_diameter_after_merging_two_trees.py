"""
Find centers

o-o-o-o-o

Topological sorting
"""

from typing import List
import collections
import math


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def build_adj_list(size, edges):
            adj_list = collections.defaultdict(list)
            for a, b in edges:
                adj_list[a].append(b)
                adj_list[b].append(a)
            return adj_list

        def find_diameter(size, adj_list):
            queue = collections.deque()
            degrees = [0] * size
            for k, v in adj_list.items():
                degrees[k] = len(v)
                if degrees[k] == 1:
                    queue.append(k)

            remaining_nodes = size
            leaves_layers_removed = 0

            while remaining_nodes > 2:

                curr_size = len(queue)
                remaining_nodes -= curr_size
                leaves_layers_removed += 1

                for _ in range(curr_size):

                    curr_node = queue.popleft()

                    for neighbor in adj_list[curr_node]:
                        degrees[neighbor] -= 1
                        if degrees[neighbor] == 1:
                            queue.append(neighbor)

            if remaining_nodes == 2:
                return 2 * leaves_layers_removed + 1
            else:
                return 2 * leaves_layers_removed

        n = len(edges1) + 1
        m = len(edges2) + 1

        adj_list1 = build_adj_list(n, edges1)
        adj_list2 = build_adj_list(m, edges2)

        diameter1 = find_diameter(n, adj_list1)
        diameter2 = find_diameter(m, adj_list2)

        combined_diameter = math.ceil(diameter1 / 2) + math.ceil(diameter2 / 2) + 1
        return max(diameter1, diameter2, combined_diameter)
