"""
Result
- Start: 1:31
- End: 1:48
- Saw solution: 1
- Solved: 1
- Optimized: 1

Idea
- Make a minimum spanning tree
  - Edge weight is the manhattan distance between two points
"""


from typing import List


# Use the same union find class implementation to many problems using union find
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.parent[x]:
            return x
        # Path compression template
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # Union by rank template
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Edges is a list of list [point_i, point_j, distance between the two]
        edges = self.generate_edges(points)

        # Sort the edges by weight (distance) in an ascending order for Kruskal's algorithm
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(size=len(points))
        ans = 0
        for i, j, distance in edges:
            # If i and j not yet connected
            # Union find uses path compression to use root node for parent node of each node
            # , so if they are connect, find() returns the same root node index
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                ans += distance
        return ans

    def generate_edges(self, points: List[List[int]]) -> List[List[int]]:
        edges = []
        for i in range(len(points)):
            # i + 1, because of undirected graph
            for j in range(i + 1, len(points)):
                edges.append([i, j, self.calculate_mahattan_distance(points[i], points[j])])
        return edges

    def calculate_mahattan_distance(self, point1: List[int], point2: List[int]) -> int:
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 20
points = [[3,12],[-2,5],[-4,1]]
# 18
points = [[0,0],[1,1],[1,0],[-1,1]]
# 4
points = [[-1000000,-1000000],[1000000,1000000]]
# 4000000
points = [[0,0]]
# 0
print(Solution().minCostConnectPoints(points))

