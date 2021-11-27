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

            # Backtract
            else:
                answer = self.traverse(query[0], query[1], set(), 1)

            answers.append(answer)

        return answers

    def traverse(self, curr_vertex: str, dest_vertex: str, visited: set, multiplier: float) -> float:
        # print(f'In traverse')
        # Initialize answer with -1.0 because there could not be edges between curr and dest,
        # even if both vertices exist in graph
        answer = -1.0
        visited.add(curr_vertex)

        neighbors = self.graph[curr_vertex]

        # If found destination, update answer
        if dest_vertex in neighbors:
            answer = neighbors[dest_vertex] * multiplier

        # If not found, traverse again
        else:
            for next_vertex, value in neighbors.items():
                # print(f'next_vertex: {next_vertex}')
                if next_vertex not in visited:
                    answer = self.traverse(next_vertex, dest_vertex, visited, value * multiplier)

                # Even if we get correct answer, for loop would overwrite the correct answer with -1.0 in the next
                # iteration in this for loop. So once we get the answer, break out of this for loop
                if answer != -1.0:
                    break

        # Remove from visited for the next query
        visited.remove(curr_vertex)
        return answer


# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Expected: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# queries = [["b", 'a']]

equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
values = [3.0,0.5,3.4,5.6]
queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
# Expected: [1.13333,16.80000,1.50000,1.00000,0.05952,2.26667,0.44118,-1.00000,-1.00000]

print(Solution().calcEquation(equations, values, queries))
