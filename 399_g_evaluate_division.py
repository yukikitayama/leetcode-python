from collections import defaultdict
from typing import List
import pprint


class Solution:
    def __init__(self):
        self.graph = None

    def calcEquation(self,
                     equations: List[List[str]],
                     values: List[float],
                     queries: List[List[str]]) -> List[float]:

        # Build the graph from the equations
        # defaultdict(default_factory=None) defaults to None
        # make one defaultdict whose default_factory is defaultdict,
        # and it nests another defaultdict whose default_factory is None
        self.graph = defaultdict(defaultdict)
        for (numerator, denominator), divided in zip(equations, values):
            self.graph[numerator][denominator] = divided
            self.graph[denominator][numerator] = 1 / divided
        # pprint.pprint(self.graph)

        # Evaluate each query by backtracking
        results = []
        for numerator, denominator in queries:
            if numerator not in self.graph or denominator not in self.graph:
                ret = -1.0
                # print(f'Query: [{numerator}, {denominator}], here')
            elif numerator == denominator:
                ret = 1.0
            else:
                visited = set()
                # Why 1?
                ret = self.backtrack(numerator, denominator, 1, visited)
            results.append(ret)

        # Return the result
        return results

    def backtrack(self,
                  curr_node: int,
                  target_node: int,
                  accumulated_product: float,
                  visited: set) -> float:
        visited.add(curr_node)
        # Initialized value if the path is not found
        ret = -1.0
        # Graph is dict of dict
        # Neighbors is dict Key: node, Value: edge weight which is product result
        neighbors = self.graph[curr_node]

        if target_node in neighbors:
            ret = accumulated_product * neighbors[target_node]

        # If target_node is not found, move forward to find target_node
        else:
            for neighbor, value in neighbors.items():
                if neighbor in visited:
                    continue
                ret = self.backtrack(neighbor, target_node, accumulated_product * value, visited)

                # If not initialized -1, backtrack found an answer
                if ret != -1.0:
                    break

        # Remove for next query
        visited.remove(curr_node)
        return ret


"""
Time complexity
Let n be the number of equations, m be the number of queries.
O(n) to make a graph, in worst case it needs to traverse all the nodes by m times so O(nm),
so O(n + nm) = O(nm)

Space complexity
O(n) for stack in backtracking, O(n) for visited set, O(n) for graph,
so O(n + n + n) = O(n)
"""



equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))

