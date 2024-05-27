"""
After performing all the union() operations, this can return the number of connected components by self.num_connected_components
union() returns boolean to let us know if we newly connected two vertices.
"""


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.num_connected_components = size

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:

            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x

            elif self.rank[parent_y] > self.rank[parent_x]:
                self.parent[parent_x] = parent_y

            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            # If all the components are connected by union, it will be 1 eventually
            self.num_connected_components -= 1

            # True as newly connected
            return True

        else:
            # False as already connected
            return False
