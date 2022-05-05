"""
- Union find
"""


from typing import List
import collections


class UnionFind:
    def __init__(self, n):
        # index is 1-based, i: 0 won't be used
        self.p = [i for i in range(n + 1)]

    def find(self, i):
        # If parent is not itself,
        # find the real parent and update
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        print(graph)

        uf = UnionFind(n)

        # Index is 1-based
        for i in range(1, n + 1):
            parent_i = uf.find(i)

            # If this parent dislikes somebody
            if parent_i in graph:

                parent_dislike_i = uf.find(graph[i][0])

                for dis in graph[i][1:]:
                    if dis < i:
                        continue
                    if not u


if __name__ == '__main__':
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(Solution().possibleBipartition(n, dislikes))
