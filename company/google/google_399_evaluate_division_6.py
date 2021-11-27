"""
- Make a graph
  - node is a variable, edge is division and inverse division
    - graph : {
      'a': {
        'b': value
      }
    }
- Initialize ans to an empty list
- Iterate each query in queries
  - if one of value in query does not belong to graph, append -1 to ans
  - if both values in query are the same, append 1 to ans
  - Otherwise find an answer from graph
    - Carry value and multiply it to a new value to do a/c = a/b * b/c
    - If there's a path between numerator denominator, append it to ans
    - If not found, append -1 to ans
    - Do DFS to traverse graph
      - Traverse from numerator to denominator
        - If found denominator, append the value to ans, break
      - visited set
      - stack
      - When no more nodes in stack, break out of DFS and append -1 to ans
    - Go to the next query
"""


from typing import List
import collections


class Solution:
    def __init__(self):
        self.graph = None

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        self.graph = collections.defaultdict(collections.defaultdict)
        for index, equation in enumerate(equations):
            self.graph[equation[0]][equation[1]] = values[index]
            self.graph[equation[1]][equation[0]] = 1 / values[index]

        ans = []

        for query in queries:

            if query[0] not in self.graph or query[1] not in self.graph:
                ans.append(-1.0)

            elif query[0] == query[1]:
                ans.append(1.0)

            else:
                divided = self.dfs(query[0], query[1], 1.0, set())
                ans.append(divided)

        return ans

    def dfs(self, curr_node: int, target_node: int, value: float, visited: set) -> float:
        visited.add(curr_node)

        result = -1

        # Get neighbors of the current node
        neighbors = self.graph[curr_node]

        # Check if we reached the destination
        if target_node in neighbors:
            curr_value = self.graph[curr_node][target_node]
            result = curr_value * value

        # If not found destination, further iterate
        else:
            for next_node, next_value in neighbors.items():

                if next_node in visited:
                    continue

                result = self.dfs(next_node, target_node, next_value * value, visited)
                if result != -1.0:
                    break

        return result


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))
