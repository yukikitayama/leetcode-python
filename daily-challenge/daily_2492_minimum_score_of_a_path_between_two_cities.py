from typing import List
import collections


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = collections.defaultdict(list)
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))

        # print(adj)

        visit = [False] * (n + 1)
        visit[1] = True

        queue = collections.deque()
        queue.append(1)

        ans = float("inf")

        while queue:

            curr = queue.popleft()

            # Not connected component
            if curr not in adj:
                continue

            for neighbor, distance in adj[curr]:
                ans = min(ans, distance)
                if not visit[neighbor]:
                    visit[neighbor] = True
                    queue.append(neighbor)

        return ans


if __name__ == "__main__":
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    n = 4
    roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]
    print(Solution().minScore(n, roads))
