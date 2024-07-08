"""
Union find
Sort logs by ascending timestamp
"""

from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.num_connected_components = size

    def find(self, x):
        if self.parent[x] == x:
            return self.parent[x]

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        uf = UnionFind(n)
        logs.sort()

        for t, x, y in logs:

            if uf.union(x, y):

                if uf.num_connected_components == 1:
                    return t

            else:
                pass

        return -1
