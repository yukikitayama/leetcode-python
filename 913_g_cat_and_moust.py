from typing import List
from collections import defaultdict


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        DRAW, MOUSE, CAT = 0, 1, 2
        color = defaultdict(int)

        degree = {}
        for m in range(N):
            for c in range(N):
                # Key is a tuple (m, c, NUM)
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - (0 in graph[c])