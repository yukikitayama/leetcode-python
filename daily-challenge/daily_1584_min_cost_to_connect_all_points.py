"""
- from approach 1 algorithm
"""


from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)

        # Return False to indicate that the current pair cannot be added to minimum spanning tree
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1

        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2

        # Default action
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        # Can return True because current pair is newly connected
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        all_edges = []

        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                all_edges.append((cost, i, j))

        # Sort by ascending cost
        all_edges.sort()

        uf = UnionFind(n)
        ans = 0
        count = 0
        for cost, i, j in all_edges:
            if uf.join(i, j):
                ans += cost
                count += 1
                if count == n - 1:
                    break

        return ans


if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    # 20
    print(Solution().minCostConnectPoints(points))
