"""
- Make graph
- If either string in query doesn't exist in graph, return -1
- DFS
- IF a path between query strings doesn't exist, return -1
"""


from typing import List
import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(collections.defaultdict)

        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1 / value

        def dfs(num, den, curr, visited):
            visited.add(num)

            ans = -1.0

            neighbors = graph[num]

            if den in neighbors:
                ans = curr * neighbors[den]

            else:
                for nei_key, nei_value in graph[num].items():

                    if nei_key in visited:
                        continue

                    ans = dfs(nei_key, den, curr * neighbors[nei_key], visited)

                    if ans != -1.0:
                        break

            visited.discard(num)

            return ans

        ans = []

        for query in queries:

            if query[0] not in graph or query[1] not in graph:
                ans.append(-1.0)

            elif query[0] == query[1]:
                ans.append(1.0)

            else:
                result = dfs(query[0], query[1], 1, set())
                ans.append(result)

            # print(f'ans: {ans}')

        return ans


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    # [6.0, 0.5, -1.0, 1.0, -1.0]
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    # [3.75000, 0.40000, 5.00000, 0.20000]
    print(Solution().calcEquation(equations, values, queries))
