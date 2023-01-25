from typing import List
import collections


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        dist1 = [float('inf')] * len(edges)
        dist2 = [float('inf')] * len(edges)

        def bfs(start, dist):
            queue = collections.deque([start])
            visited = [False] * len(edges)
            dist[start] = 0

            while queue:

                curr = queue.popleft()

                if visited[curr]:
                    continue

                visited[curr] = True
                neighbor = edges[curr]
                if neighbor != -1 and not visited[neighbor]:
                    dist[neighbor] = 1 + dist[curr]
                    queue.append(neighbor)

        bfs(node1, dist1)
        bfs(node2, dist2)

        # print(dist1)
        # print(dist2)

        ans = -1
        curr_min = float('inf')
        for i in range(len(edges)):
            if max(dist1[i], dist2[i]) < curr_min:
                curr_min = max(dist1[i], dist2[i])
                # Smallest index will be stored
                ans = i

        return ans


if __name__ == "__main__":
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    print(Solution().closestMeetingNode(edges, node1, node2))


