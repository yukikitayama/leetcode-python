"""
Idea
- Backtracking
  - In traversal,
    - count the number of nodes visited
    - increment the total cost
  - When the number of visited nodes is equal to n
    - update minimum total cost
- If the max count of visited node not reaching n, return -1
  - Otherwise, return minimum total cost

Solution
- Use minimum spanning tree by kruskal's algorithm
  - Connect all the nodes with the minimum possible total weight

Complexity
- Let n be the number of cities, and m be the number of edges
- Time is O(mlogm) for sorting connections. union() takes logn, and we do it
  for each connections m, so O(mlogn)
- Space is O(n) to keep parents array and weights array in an object of Disjoint Set
"""


from typing import List


class DisjointSet:
    def __init__(self, n):
        # +1 for convenience
        # cities are from 1 to n
        # if we use city number to access array, no need to do -1
        self.weights = [1] * (n + 1)
        self.parents = [i for i in range(n + 1)]

    def find(self, a):
        # Path compression
        while a != self.parents[a]:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a

    # Check if they have the same parents
    # If they have the same parents, they belong to the same group
    def is_in_same_group(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        # If a and b are already in the same group,
        # we don't need to do anything
        if root_a == root_b:
            return

        # Weighted union
        if self.weights[root_a] > self.weights[root_b]:
            self.parents[root_b] = root_a
            self.weights[root_a] += self.weights[root_b]

        else:
            self.parents[root_a] = root_b
            self.weights[root_b] += self.weights[root_a]


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])

        # print(f'connections:')
        # [print(connection) for connection in connections]

        count = 0
        cost = 0
        disjoint_set = DisjointSet(n)

        for i in range(len(connections)):
            a = connections[i][0]
            b = connections[i][1]

            # If they are already in the same group, skip it because
            # we don't wanna make a cycle
            if disjoint_set.is_in_same_group(a, b):
                continue

            # Make them belong to the same group
            disjoint_set.union(a, b)

            # Increment the cost
            cost += connections[i][2]

            # Increment the number of visited cities
            count += 1

        # n - 1 because count is incremented when connecting cities.
        # with n cities, there are n - 1 connectings. e.g. 2 cities, only 1 connecting
        if count == n - 1:
            return cost
        # Otherwise we couldn't visit all the cities
        else:
            return -1


n = 3
connections = [[1,2,5],[1,3,6],[2,3,1]]
n = 4
connections = [[1,2,3],[3,4,4]]
print(Solution().minimumCost(n, connections))







