"""
Graph
Edge is abs x distance <= source r and abs y distance <= source r
DFS

If the Euclidean distance <= source r, detonate target
"""

from typing import List
import collections


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def compute_euclidean_distance(a, b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

        graph = collections.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):

                if i == j:
                    continue

                source = [bombs[i][0], bombs[i][1]]
                r = bombs[i][2]

                target = [bombs[j][0], bombs[j][1]]

                d = compute_euclidean_distance(source, target)

                if d <= r:
                    graph[i].append(j)

        # print(graph)

        def dfs(curr):
            nonlocal count
            visited.add(curr)
            count += 1
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    dfs(neighbor)

        ans = 0

        for i in range(len(bombs)):
            visited = set()
            count = 0
            dfs(i)
            ans = max(ans, count)

        return ans


if __name__ == "__main__":
    bombs = [[2, 1, 3], [6, 1, 4]]
    # 2
    bombs = [[1, 1, 5], [10, 10, 5]]
    # 1
    # bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    # 5
    print(Solution().maximumDetonation(bombs))






