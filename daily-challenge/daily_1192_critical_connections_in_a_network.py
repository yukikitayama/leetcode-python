"""
- An edge is a critical connection, if and only if it's not in cycle
- Find all the cycles in graph
- Discard all the edges belonging to such cycles
- Track visited node and if visit again, cycle detected
"""


from typing import List
import collections


class Solution:
    def __init__(self):
        self.rank = {}
        self.graph = collections.defaultdict(list)
        # ?
        self.conn_dict = {}

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.form_graph(n, connections)

        # print('did form_graph()')
        # print(f'rank: {self.rank}, graph: {self.graph}, conn_dict: {self.conn_dict}')

        self.dfs(0, 0)

        # print('did dfs()')
        # print(f'conn_dict: {self.conn_dict}')

        ans = []
        for u, v in self.conn_dict:
            ans.append([u, v])

        return ans

    def form_graph(self, n: int, connections: List[List[int]]):

        for i in range(n):
            self.rank[i] = None

        for edge in connections:

            # Make bidirectional edges
            u, v = edge

            self.graph[u].append(v)
            self.graph[v].append(u)

            # ?
            self.conn_dict[(min(u, v), max(u, v))] = 1

    def dfs(self, node: int, discovery_rank: int) -> int:

        # If already rank is assigned
        if self.rank[node]:
            return self.rank[node]

        self.rank[node] = discovery_rank

        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:

            # ?
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            # Check if this edge needs to be discarded
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]

            min_rank = min(min_rank, recursive_rank)

        return min_rank


if __name__ == '__main__':
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(Solution().criticalConnections(n, connections))
