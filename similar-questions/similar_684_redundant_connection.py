"""

"""


from typing import List


class DSU:
    # def __init__(self):
    def __init__(self, length):
        # Constraints says 3 <= n <= 1000
        # 1001 for convenience by not using the index 0
        # Initialize all the indices as itself being the leader

        # self.par = [i for i in range(1001)]
        # self.rnk = [0] * 1001

        self.par = [i for i in range(length + 1)]
        self.rnk = [0] * (length + 1)

    # Find a leader index
    def find(self, x):
        # If x is not leader in the set,
        # par[x] gives us the leader index, find(leader index) gives us the leader index
        # we put leader index to par[x], because we might have situation where
        # leader -> intermediate -> intermediate -> x, but this will be
        # leader -> x
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        # If x is leader in the set, just return own index x
        return self.par[x]

    # Connect x and y
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        # If x and y are already connected return False
        if xr == yr:

            # print(f'Already connected x: {x}, y: {y}, self.par: {self.par}, self.rnk: {self.rnk}')

            return False

        # If y has more followers, x's leader is y
        elif self.rnk[xr] < self.rnk[yr]:

            # print(f'  y has more followers')

            self.par[xr] = yr

        # If x has more followers, y's leader is x
        elif self.rnk[xr] > self.rnk[yr]:

            # print(f'  x has more followers')

            self.par[yr] = xr

        # Otherwise
        else:

            # print(f'  Both are not connected')

            # y follows x
            self.par[yr] = xr
            # Increment x's followers
            self.rnk[xr] += 1

        # print(f'Connect x: {x}, y: {y}, self.par: {self.par}, self.rnk: {self.rnk}')

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dsu = DSU()
        dsu = DSU(length=len(edges))

        for edge in edges:
            # union() returns False when the two edges are alread connected
            # If not False is True
            if not dsu.union(edge[0], edge[1]):
                return edge


edges = [[1,2],[1,3],[2,3]]
print(Solution().findRedundantConnection(edges))
