"""
- Top down dynamic programming
"""


from typing import List
import functools


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        @functools.lru_cache(maxsize=None)
        def all_paths_to_target(curr):

            print(f'  all_path_to_target({curr})')

            if curr == len(graph) - 1:

                print(f'    return {[[len(graph) - 1]]}, curr: {curr}')

                # [[]] to allow the for loop and list concatenation to work
                return [[len(graph) - 1]]

            results = []
            for next in graph[curr]:

                print(f'  next: {next}')

                for path in all_paths_to_target(next):
                    results.append([curr] + path)

            print(f'    return {results}, curr: {curr}')

            return results

        return all_paths_to_target(0)


graph = [[1,2],[3],[3],[]]
# print(len(graph))
graph = [[4,3,1],[3,2,4],[3],[4],[]]
graph = [[1],[]]
graph = [[1, 2, 3], [2], [3], []]
graph = [[1,3],[2],[3],[]]
graph = [[1, 2], [2], []]
print(Solution().allPathsSourceTarget(graph))



