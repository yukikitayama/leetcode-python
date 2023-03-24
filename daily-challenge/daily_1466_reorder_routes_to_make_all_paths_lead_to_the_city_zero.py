from typing import List
import collections


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj = collections.defaultdict(list)
        for a, b in connections:
            # Parent to child, so need to flip
            adj[a].append((b, 1))
            # Child to parent, so no need to flip
            adj[b].append((a, 0))

        ans = 0

        def dfs(node, parent):

            nonlocal ans

            if node not in adj:
                return

            for neighbor_node, neighbor_direction in adj[node]:
                if neighbor_node != parent:
                    ans += neighbor_direction
                    dfs(neighbor_node, node)

        dfs(0, -1)

        return ans


