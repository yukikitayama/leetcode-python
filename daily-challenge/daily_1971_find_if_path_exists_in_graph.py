from typing import List
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [source]
        visited = set([source])

        while stack:

            curr = stack.pop()

            if curr == destination:
                return True

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return False


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2

    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5

    print(Solution().validPath(n, edges, source, destination))



