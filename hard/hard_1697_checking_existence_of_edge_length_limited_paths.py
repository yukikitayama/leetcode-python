"""
Dijkstra's algorithm?

Ans
  union find
"""

from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x

            elif self.rank[parent_y] > self.rank[parent_x]:
                self.parent[parent_x] = parent_y

            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

    def are_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        edgeList.sort(key=lambda x: (x[2]))
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x: (x[2]))

        # print(edgeList)
        # print(queries)

        ans = [False] * len(queries)
        uf = UnionFind(n)
        edge_index = 0

        for p, q, limit, query_index in queries:

            while edge_index < len(edgeList) and edgeList[edge_index][2] < limit:
                u = edgeList[edge_index][0]
                v = edgeList[edge_index][1]
                uf.union(u, v)
                edge_index += 1

            if uf.are_connected(p, q):
                ans[query_index] = True

        return ans
