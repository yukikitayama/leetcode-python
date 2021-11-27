"""
- Make a disjoint set object
- From isConnected, perform union
- Return the number of nodes whose index is the root index
  - Because index itself is not equal to root index, this index belongs to a province
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
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

            # Initially count is the number of nodes
            # Every time it unions two nodes, they form a province,
            # so we lose one node from the distinct separate nodes
            self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # Make disjoint set object
        disjoint_set = DisjointSet(n)

        for row in range(n):
            # row + 1 because isConnected matrix is symmetric by diagonal,
            # and diagonal is not a necessary information
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    # Union
                    disjoint_set.union(row, col)

        # Return the number of sets
        return disjoint_set.get_count()


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))

