from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = None

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(defaultdict)
        for i, equation in enumerate(equations):
            self.graph[equation[0]][equation[1]] = values[i]
            self.graph[equation[1]][equation[0]] = 1 / values[i]

        answers = []

        for query in queries:
            if query[0] not in self.graph or query[1] not in self.graph:
                answer = -1.0
            elif query[0] == query[1]:
                answer = 1.0
            else:
                # Traverse graph
                answer = self.traverse(query[0], query[1], 1.0, set())
            answers.append(answer)

        return answers

    def traverse(self, curr_vertex: str, dest_vertex: str, multiplier: float, visited: set) -> float:
        visited.add(curr_vertex)
        answer = -1.0

        neighbors = self.graph[curr_vertex]

        if dest_vertex in neighbors:
            answer = neighbors[dest_vertex] * multiplier

        else:
            for next_vertex, value in neighbors.items():
                if next_vertex in visited:
                    continue
                answer = self.traverse(next_vertex, dest_vertex, value * multiplier, visited)

                if answer != -1:
                    break

        visited.remove(curr_vertex)
        return answer


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))

