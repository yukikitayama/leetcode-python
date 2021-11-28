"""
Idea
- Make an adjacency list as graph first
- DFS in the graph
  - If current vertex is target, return False
  - If after all the iterations, it didn't reach the target, no path exist, so return False

Complexity
- Time is O(V + E) because it needs to check every vertex and traverse through every edge
- Space is O(V) for the recursion call stack
"""


from typing import List
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        # Make an adjacency matrix first to let DFS traverse easy
        curr_to_neighbors = collections.defaultdict(list)
        for edge in edges:
            curr_to_neighbors[edge[0]].append(edge[1])
            curr_to_neighbors[edge[1]].append(edge[0])

        def dfs(curr: int, target: int, visited: set) -> bool:

            if curr == target:
                return True

            for neighbor in curr_to_neighbors[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # If this condition is True, target is found, so return True
                    if dfs(neighbor, target, visited):
                        return True

            # Otherwise the target was not found, return False
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



