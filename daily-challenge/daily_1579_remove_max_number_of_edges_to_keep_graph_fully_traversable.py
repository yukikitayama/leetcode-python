from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.num_connected_components = size

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

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

            self.num_connected_components -= 1

            return True

        else:
            return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        uf_a = UnionFind(n)
        uf_b = UnionFind(n)

        required_edge = 0

        # Type 3
        for type_, u, v in edges:
            u -= 1
            v -= 1

            if type_ == 3:
                res_a = uf_a.union(u, v)
                res_b = uf_b.union(u, v)

                if res_a or res_b:
                    required_edge += 1

        for type_, u, v in edges:
            u -= 1
            v -= 1

            if type_ == 1:
                res_a = uf_a.union(u, v)
                if res_a:
                    required_edge += 1

            if type_ == 2:
                res_b = uf_b.union(u, v)
                if res_b:
                    required_edge += 1

        if uf_a.num_connected_components == 1 and uf_b.num_connected_components == 1:
            return len(edges) - required_edge
        else:
            return -1
