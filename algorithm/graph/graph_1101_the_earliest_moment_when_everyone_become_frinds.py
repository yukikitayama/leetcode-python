"""
Result
- Start: 1:59
- End: 2:11
- Solved: 1
- Optimized: 1
- Saw solution: 0

Idea
- Indirect connection exists
- Make a class of Disjoint set
- Initialize with count n
- Sort logs by first element in an ascending order
- Do union to each log in logs
- When count becomes 1, return the timestamp
- Otherwise, at the end, return -1
"""


from typing import List


class DisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x
        # Path compression
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

            self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        djs = DisjointSet(n)

        for t, x, y in logs:

            djs.union(x, y)

            if djs.get_count() == 1:
                return t

        return -1


logs = [
    [20190101, 0, 1],
    [20190104, 3, 4],
    [20190107, 2, 3],
    [20190211, 1, 5],
    [20190224, 2, 4],
    [20190301, 0, 3],
    [20190312, 1, 2],
    [20190322, 4, 5]
]
n = 6
# 20190301
logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
n = 4
# 3
print(Solution().earliestAcq(logs, n))


