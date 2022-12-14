from typing import List
import collections


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        visited = [False] * n

        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i):

            nonlocal ans

            visited[i] = True

            for neighbor in graph[i]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(len(visited)):
            if not visited[i]:
                ans += 1
                dfs(i)

        return ans


if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(Solution().countComponents(n, edges))
