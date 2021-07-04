from typing import List
from collections import deque


class Solution:
    def __init(self):
        self.graph = None
        self.target = None
        self.results = None

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.target = len(graph) - 1
        self.results = []

        path = deque([0])
        self.backtrack(0, path)

        return self.results

    def backtrack(self, currNode, path):
        if currNode == self.target:
            self.results.append(list(path))
            return

        for nextNode in self.graph[currNode]:
            path.append(nextNode)
            self.backtrack(nextNode, path)
            path.pop()
