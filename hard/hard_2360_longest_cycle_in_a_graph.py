from typing import List
import collections


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        indegree = [0] * len(edges)
        for edge in edges:
            if edge != -1:
                indegree[edge] += 1

        # Find nodes which can be start node of Kahn's algorithm
        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        # Run Kahn's algorithm to identify nodes which cannot visit
        visited = [False] * len(edges)
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            neighbor = edges[curr]
            if neighbor != -1:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # print(visited)
        # print(indegree)

        # Traverse from the nodes that cannot be visited by Kahn's algorithm
        # and compute the distance
        ans = -1

        for i in range(len(visited)):
            if not visited[i]:
                neighbor = edges[i]
                count = 1
                visited[i] = True
                # Keep iterating until coming back
                while neighbor != i:
                    visited[neighbor] = True
                    count += 1
                    neighbor = edges[neighbor]

                # Count of nodes in a cycle is equal to the total distance of edeges
                # if there are 3 nodes in a cycle, there are 3 edges in the cycle
                ans = max(ans, count)

        return ans

    def longestCycle1(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n

        ans = -1

        def dfs(node, dist):
            # print(f"node: {node}, dist: {dist}")
            nonlocal ans

            visited[node] = True

            neighbor = edges[node]

            if neighbor != -1 and not visited[neighbor]:
                dist[neighbor] = dist[node] + 1
                dfs(neighbor, dist)

            elif neighbor != -1 and neighbor in dist:
                # print(f"  node: {node}, dist: {dist}")
                # dist[node] - dist[neighbor] is the distance from previous node to current node
                # +1 is the distance from current to previous node to circle back
                ans = max(ans, dist[node] - dist[neighbor] + 1)

        for i in range(n):
            if not visited[i]:
                dist = {i: 0}
                dfs(i, dist)

        return ans