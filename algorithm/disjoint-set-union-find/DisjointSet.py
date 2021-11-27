class DisjointSet:
    def __init__(self, size):
        # This assumes node is 0-based.
        # e.g. size: 3, node: {0, 1, 2}
        self.parent = [i for i in range(size)]
        # If node starts from 1, should use the below and ignore 0 index
        # self.parent = [i for i in range(size + 1)]

        # Initially all the nodes are isolated with size itself, so initialized with 1
        self.rank = [1] * size

    def find(self, x):
        # If x is the root node, no need to do path compression
        if x == self.root[x]:
            return x
        # Path compression to update parent node with root node
        # The below initiates recursion
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        # If roots are the same, no need to do connect them
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                # No need to update rank because smaller height comes down to bigger height,
                # so height does not change. But in else block, the height does change.
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            # Otherwise either root can be a new root
            # Choose x to be the root
            else:
                self.parent[root_y] = root_x
                # If x and y ranks are the same, it means they have the same height
                # But now either comes down to the other root, so the height increase by 1
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
