"""
clieque: complete connected component
"""

from typing import List
import collections


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] > self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        return True


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        component_id_to_edge_count = collections.Counter()

        for a, b in edges:
            uf.union(a, b)

        for a, b in edges:
            root = uf.find(a)
            component_id_to_edge_count[root] += 1

        ans = 0
        for vertex in range(n):
            if uf.find(vertex) == vertex:
                node_count = uf.size[vertex]
                expected_edges = (node_count * (node_count - 1)) // 2
                if component_id_to_edge_count[vertex] == expected_edges:
                    ans += 1

        return ans
