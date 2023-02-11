"""
- BFS
"""


from typing import List
import collections


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        adj = collections.defaultdict(list)

        # 0 as red
        for from_, to_ in redEdges:
            adj[from_].append([to_, 0])

        # 1 as blue
        for from_, to_ in blueEdges:
            adj[from_].append([to_, 1])

        # print(adj)

        ans = [-1] * n
        ans[0] = 0

        visit = [[False] * 2 for _ in range(n)]
        visit[0][0] = True
        visit[0][1] = True

        queue = collections.deque()
        queue.append((0, 0, -1))

        while queue:
            node, step, prev_color = queue.popleft()

            if node not in adj:
                continue

            for neighbor, color in adj[node]:

                if not visit[neighbor][color] and color != prev_color:

                    if ans[neighbor] == -1:
                        ans[neighbor] = step + 1

                    visit[neighbor][color] = True

                    queue.append((neighbor, step + 1, color))

        return ans


if __name__ == "__main__":
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []
    # [0, 1, -1]

    n = 3
    redEdges = [[0, 1]]
    blueEdges = [[2, 1]]
    # [0, 1, -1]

    print(Solution().shortestAlternatingPaths(n, redEdges, blueEdges))
