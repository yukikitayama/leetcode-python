"""
- Union find
"""


from typing import List
import collections


class UnionFind:
    def __init__(self, num_cell):
        self.count = 0
        self.parent = [-1] * num_cell
        self.rank = [0] * num_cell

    def is_valid(self, i) -> bool:
        return self.parent[i] >= 0

    def set_parent(self, i) -> None:
        # print(f'i: {i}, self.parent[i]: {self.parent[i]}')

        # Positions could have duplicates. That case, it won't count up and won't update parent
        if self.parent[i] != -1:
            return

        self.parent[i] = i
        self.count += 1

    # Path compression
    def find(self, i) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.parent[root_x] = root_y
            else:
                # If ranks are the same, by default, use x
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

            # x and y were separate islands, but it unioned now, so
            # the number of islands decreased by 2 islands -> 1 island
            self.count -= 1

    def get_count(self) -> int:
        return self.count


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        uf = UnionFind(m * n)

        for position in positions:
            r, c = position
            overlap = []

            # is_valid() checks if parent[island] is greater than or equal to 0
            # If it's true, the island already exists as one island or belong to an island
            if r - 1 >= 0 and uf.is_valid((r - 1) * n + c):
                overlap.append((r - 1) * n + c)
            if r + 1 < m and uf.is_valid((r + 1) * n + c):
                overlap.append((r + 1) * n + c)
            if c - 1 >= 0 and uf.is_valid(r * n + c - 1):
                overlap.append(r * n + c - 1)
            if c + 1 < n and uf.is_valid(r * n + c + 1):
                overlap.append(r * n + c + 1)

            index = r * n + c
            uf.set_parent(index)
            for i in overlap:
                uf.union(i, index)
            ans.append(uf.get_count())

        return ans


"""
- Key of land_to_id is calculated by current row * n + current col

Complexity
- Time is O(l) by letting l the length of positions
- Space is O(l) for hashmap
"""


m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]
# Output: [1,1,2,3]
m = 1
n = 1
positions = [[0,0]]
# Output: [1]
m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[1,2]]
# Output: [1,1,2,2]
"""
positions could not be unique
0   *   *
1           *
2
    0   1   2
"""
print(Solution().numIslands2(m, n, positions))
