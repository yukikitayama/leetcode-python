from typing import List
from collections import defaultdict
import pprint


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Initialize dictionary value as set
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        # pprint.pprint(graph)

        count = [1] * n
        answer = [0] * n

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return answer

n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(Solution().sumOfDistancesInTree(n, edges))
