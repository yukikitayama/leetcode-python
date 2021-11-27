"""


Algorithm
- iterate each edge in edges
  - Do union() to current edge
    - union() returns True, if there were not connected (in the same set) and connect now
    - union() returns False if there were already in the same set,
      - Append the current False edge to answer list and return
- union(edge[0], edge[1])
  - find x, and y
"""


from typing import List


class DSU:
    def __init__(self):
        self.par = [i for i in range(1001)]
        self.rnk = [0] * 1001

    def find(self, x):
        # If x is not the parent
        if self.par[x] != x:
            # Find the index of parent of x and
            # set x's index to parent
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        # If their leader is the same, x and y are already in the same set
        if xr == yr:
            return False

        # If y has more member, y is the leader
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr

        # If x has more member, x is the leader
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr

        # Otherwise this is the first time to call find to x and y
        else:
            # If xr and yr are not the same, we connect
            self.par[yr] = xr
            self.rnk[xr] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = DSU()

        for edge in edges:
            if dsu.union(edge[0], edge[1]):
                continue
            else:
                return edge





