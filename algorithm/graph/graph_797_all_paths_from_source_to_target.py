from typing import List
import collections


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        if not graph or not len(graph):
            return ans

        queue = collections.deque([[0]])

        while queue:

            curr_path = queue.popleft()
            last_node = curr_path[-1]

            for next_node in graph[last_node]:
                tmp = curr_path[:]
                tmp.append(next_node)

                if next_node == len(graph) - 1:
                    ans.append(tmp)
                else:
                    queue.append(tmp)

        return ans


graph = [[1,2],[3],[3],[]]
print(Solution().allPathsSourceTarget(graph))
