"""
Tree
  no cycle
  Fully connected
  n - 1 edges

Each time there was no merge, it was because we were adding an edge between two nodes that were already connected via a path.
"""

from typing import List



class DSU:
    def __init__(self, n):
        self.rank = [1 for _ in range(n)]
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

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        dsu = DSU(n)

        for a, b in edges:
            res = dsu.union(a, b)
            if not res:
                return False

        return True