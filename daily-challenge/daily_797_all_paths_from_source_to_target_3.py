from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def backtracking(curr_index, curr_list):

            if curr_index == n - 1:
                ans.append(curr_list[:])

            for next_index in graph[curr_index]:
                curr_list.append(next_index)
                backtracking(next_index, curr_list)
                curr_list.pop()

        backtracking(0, [0])
        return ans


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(Solution().allPathsSourceTarget(graph))
