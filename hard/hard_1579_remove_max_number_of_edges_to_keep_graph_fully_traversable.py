"""
Obs
  make sense to keep type 3, and remove type 1 or type 2

Ans
  think we have 2 graphs
    Alice graph type 1 and 3
    Bob graph type 2 and 3
"""

from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.num_connected_components = size

    def find(self, x):
        if x == self.parent[x]:
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

            # If all the components are connected by union, it will be 1 eventually
            self.num_connected_components -= 1

            # True as newly connected
            return True

        else:
            # False as already connected
            return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        required_edge = 0

        # Type 3 first
        for type_, u, v in edges:
            u -= 1
            v -= 1

            if type_ == 3:

                res_alice = uf_alice.union(u, v)
                res_bob = uf_bob.union(u, v)

                if res_alice or res_bob:
                    required_edge += 1

        # Type 1 and 2
        for type_, u, v in edges:
            u -= 1
            v -= 1

            if type_ == 1:
                res_alice = uf_alice.union(u, v)
                if res_alice:
                    required_edge += 1

            elif type_ == 2:
                res_bob = uf_bob.union(u, v)
                if res_bob:
                    required_edge += 1

        print(required_edge)

        # Check connected
        if uf_alice.num_connected_components == 1 and uf_bob.num_connected_components == 1:
            return len(edges) - required_edge

        else:
            return -1

