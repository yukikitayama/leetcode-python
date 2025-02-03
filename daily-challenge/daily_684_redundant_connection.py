from typing import List
import collections


class DSU:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        else:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
            return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = DSU(len(edges))

        for a, b in edges:

            res = dsu.union(a - 1, b - 1)

            if not res:
                return [a, b]

        return []

    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        def is_connected(src, dst, visited):
            visited[src] = True

            if src == dst:
                return True

            is_found = False
            for neighbor in adj[src]:
                if not visited[neighbor]:
                    is_found = is_found or is_connected(neighbor, dst, visited)

            return is_found

        for a, b in edges:
            visited = [False] * len(edges)
            if is_connected(a - 1, b - 1, visited):
                return [a, b]

            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)