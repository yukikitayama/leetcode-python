from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_size = 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_size = max(self.max_size, self.size[root_x])
            return True

        return False


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = [edge[:] for edge in edges]

        for i, edge in enumerate(new_edges):
            edge.append(i)

        # Sort by weights
        new_edges.sort(key=lambda x: x[2])

        # Find MST weight using union find
        uf = UnionFind(n)
        std_weight = 0
        for u, v, w, _ in new_edges:
            if uf.union(u, v):
                std_weight += w

        print(f"std_weight: {std_weight}")

        # Check each edge if it's critical and pseudo-critical
        critical = []
        pseudo_critical = []
        for u, v, w, i in new_edges:
            uf_ignore = UnionFind(n)
            ignore_weight = 0
            for x, y, w_ignore, j in new_edges:
                if i != j and uf_ignore.union(x, y):
                    ignore_weight += w_ignore

            if uf_ignore.max_size < n or ignore_weight > std_weight:
                critical.append(i)
                # Skip pseudo critical
                continue

            uf_force = UnionFind(n)
            force_weight = w
            uf_force.union(u, v)
            for x, y, w_force, j in new_edges:
                if i != j and uf_force.union(x, y):
                    force_weight += w_force

            if force_weight == std_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]