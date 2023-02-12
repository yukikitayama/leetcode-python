from typing import List
import collections
import math


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        adj = collections.defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        ans = 0

        def dfs(node, parent):
            nonlocal ans

            if node not in adj:
                return 1

            rep = 1

            for child in adj[node]:
                if child != parent:
                    rep += dfs(child, node)

            if node != 0:
                ans += math.ceil(rep / seats)

            return rep

        dfs(0, -1)

        return ans


if __name__ == "__main__":
    roads = [[0, 1], [0, 2], [0, 3]]
    seats = 5
    print(Solution().minimumFuelCost(roads, seats))

