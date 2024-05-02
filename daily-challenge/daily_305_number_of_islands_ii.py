"""
Increment number of islands every time add a land
Decrement number of islands every time merge occurs
"""

from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [0] * size
        self.count = 0

    def add_land(self, x):

        # Edge: already created land
        if self.parent[x] >= 0:
            return

        self.parent[x] = x
        self.count += 1

    def is_land(self, x):
        if self.parent[x] >= 0:
            return True
        else:
            return False

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        x_r = self.find(x)
        y_r = self.find(y)

        # If it's already merged
        if x_r == y_r:
            return

        elif self.rank[x_r] < self.rank[y_r]:
            self.parent[x_r] = y_r

        elif self.rank[x_r] > self.rank[y_r]:
            self.parent[y_r] = x_r

        else:
            self.parent[y_r] = x_r
            self.rank[x_r] += 1

        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        uf = UnionFind(m * n)

        ans = []

        for position in positions:
            # Convert matrix index to array index
            land_position = position[0] * n + position[1]

            uf.add_land(land_position)

            for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_r = position[0] + offset_r
                neighbor_c = position[1] + offset_c

                neighbor_position = neighbor_r * n + neighbor_c

                # By adding current land, if we need to merge lands
                if 0 <= neighbor_r < m and 0 <= neighbor_c < n and uf.is_land(neighbor_position):
                    uf.union(land_position, neighbor_position)

            ans.append(uf.count)

        return ans