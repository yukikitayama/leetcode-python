from typing import List
from collections import defaultdict


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
            print()
            print(f'query: {numerator, denominator}')

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
        print(f'target_node: {target_node}, visited: {visited}')
        visited.remove(curr_node)
        return ret


# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
print(Solution().calcEquation(equations, values, queries))
