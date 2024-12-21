from typing import List
import collections


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0

        def dfs(current_node, parent_node):
            nonlocal ans

            sum_ = 0
            for neighbor_node in graph[current_node]:
                if neighbor_node != parent_node:
                    sum_ += dfs(neighbor_node, current_node)
                    sum_ %= k

            sum_ += values[current_node]
            sum_ %= k

            if sum_ == 0:
                ans += 1

            return sum_

        dfs(0, -1)

        return ans