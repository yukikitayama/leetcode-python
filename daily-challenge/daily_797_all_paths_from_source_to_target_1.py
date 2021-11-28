"""
Result
- Start: 7:26
- End: 7:27
- Solved: 1
- Saw solution: 0
- Optimized: 1

Idea
- Backtracking
- Use graph object as a adjacency list

Complexity
- Every time we add a new node to the graph, the number of paths would double
- Time
  - At maximum, every time path doubles, so 2^n number of path, and at most n -2 intermediate nodes
  - O(n * 2^n)
- Space is O(n) for the recursion stack
"""


from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def backtracking(start, curr):
            if start == len(graph) - 1:
                ans.append(curr[:])
                return

            for next in graph[start]:
                curr.append(next)
                backtracking(next, curr)
                curr.pop()

            return

        ans = []

        backtracking(0, [0])

        return ans


graph = [[1,2],[3],[3],[]]
# print(len(graph))
graph = [[4,3,1],[3,2,4],[3],[4],[]]
graph = [[1],[]]
graph = [[1, 2, 3], [2], [3], []]
graph = [[1,3],[2],[3],[]]
print(Solution().allPathsSourceTarget(graph))



