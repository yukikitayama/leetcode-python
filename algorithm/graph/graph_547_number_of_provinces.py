"""
- Make a disjoint set object
- From isConnected, perform union
- Return the number of distinct parent nodes
"""


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [-1] * len(isConnected)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    self.union(parent, i, j)
        ans = 0
        for i in range(len(parent)):
            if parent[i] == -1:
                ans += 1
        return ans

    def union(self, parent, x, y):
        # If parent is initialized -1 value, returns the node itself
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        # Union by updating -1 with node value
        if root_x != root_y:
            parent[root_x] = root_y

    def find(self, parent, x):
        if parent[x] == -1:
            return x
        root = self.find(parent, parent[x])
        return root


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))

