"""
Result
- Start: 11:15
- End: 11:22
- Solved: 1
- Saw solution: 0
- Optimized: 1

Idea
- Make an adjacency graph
- Traverse

Complexity
- Time is O(V + E) because it needs to check every vertex and traverse through every edge
- Space is O(V) for the recursion call stack
"""


from typing import List
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        vertex_to_neighbors = collections.defaultdict(list)
        for edge in edges:
            vertex_to_neighbors[edge[0]].append(edge[1])
            vertex_to_neighbors[edge[1]].append(edge[0])

        # print(f'{vertex_to_neighbors}')

        def dfs(curr, target, visited):

            if curr == target:
                return True

            for neighbor in vertex_to_neighbors[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor, target, visited):
                        return True

            return False

        return dfs(start, end, set())


n = 3
edges = [[0,1],[1,2],[2,0]]
start = 0
end = 2
# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# start = 0
# end = 5
print(Solution().validPath(n, edges, start, end))



