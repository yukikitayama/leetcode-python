from typing import List
import collections


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        indegree = [0] * n
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1

        count = [[0] * 26 for _ in range(n)]
        queue = collections.deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        ans = 1
        nodes_seen = 0

        while queue:
            node = queue.popleft()

            count[node][ord(colors[node]) - ord("a")] += 1
            ans = max(ans, count[node][ord(colors[node]) - ord("a")])
            nodes_seen += 1

            if node not in adj:
                continue

            for neighbor in adj[node]:

                for i in range(26):

                    count[neighbor][i] = max(count[neighbor][i], count[node][i])

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return -1 if nodes_seen < n else ans


if __name__ == "__main__":
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]
    print(Solution().largestPathValue(colors, edges))

