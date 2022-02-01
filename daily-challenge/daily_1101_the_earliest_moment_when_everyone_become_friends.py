"""
- Disjoint set to connect friends
- Sort logs by timestamp in an ascending order
"""


from typing import List


class DisjointSet:
    def __init__(self, n):
        # Number of disjoint set
        self.count = n
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, i):
        if i == self.parent[i]:
            return i
        # path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)

        if xr != yr:
            if self.rank[xr] > self.rank[yr]:
                self.parent[yr] = xr
            elif self.rank[xr] < self.rank[yr]:
                self.parent[xr] = yr
            else:
                self.parent[yr] = xr
                self.rank[xr] += 1
            self.count -= 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        disjoint_set = DisjointSet(n)

        for t, x, y in logs:
            disjoint_set.union(x, y)

            # If everyone connected
            if disjoint_set.count == 1:
                return t

        return -1


if __name__ == '__main__':
    logs = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
            [20190312, 1, 2], [20190322, 4, 5]]
    n = 6
    print(Solution().earliestAcq(logs, n))
