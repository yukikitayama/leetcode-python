"""
- Time: 7m
- Solved: 1
- Saw solution: 0
- Optimized: 1
"""


from typing import List
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_list = collections.defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        queue = collections.deque([start])
        visited = {start}

        # print(adj_list)

        while queue:

            curr = queue.popleft()

            if curr == end:
                return True

            if curr in adj_list:
                for neighbor in adj_list[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        return False


n = 3
edges = [[0,1],[1,2],[2,0]]
start = 0
end = 2
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
start = 0
end = 5
print(Solution().validPath(n, edges, start, end))
