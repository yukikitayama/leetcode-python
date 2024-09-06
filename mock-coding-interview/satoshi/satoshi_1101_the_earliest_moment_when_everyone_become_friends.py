"""
acquainted
  a - c - b, a is acquainted with b

disjoint set (union find)
"""

from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.num_group = size

    def find(self, x):
        return self.find(self.parent[x]) if self.parent[x] != x else self.parent[x]

    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)

        if r_x != r_y:

            if self.rank[r_x] > self.rank[r_y]:
                self.parent[r_y] = r_x
                self.rank[r_x] += 1
            elif self.rank[r_x] < self.rank[r_y]:
                self.parent[r_x] = r_y
                self.rank[r_y] += 1
            else:
                self.parent[r_y] = r_x
                self.rank[r_x] += 1

            self.num_group -= 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        logs.sort()

        uf = UnionFind(size=n)

        for t, x, y in logs:

            # If not, union x and y
            uf.union(x, y)

            # Check whether the current number of groups is 1
            if uf.num_group == 1:
                return t

        # Impossible to every body friends, war, global peace
        return -1