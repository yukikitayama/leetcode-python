from typing import List
import collections


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = [-1] * (n + 1)

        def bfs(source):

            # print(f'source: {source}')

            queue = collections.deque([source])
            colors[source] = 0

            while queue:

                curr = queue.popleft()

                # print(f'  curr: {curr}, colors: {colors}')

                for neighbor in graph[curr]:

                    # print(f'    neighbor: {neighbor}')

                    # If already color is assigned previously and the same color
                    if colors[neighbor] != -1 and colors[curr] == colors[neighbor]:
                        return False

                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[curr]
                        queue.append(neighbor)

            return True

        for i in range(1, len(colors)):
            if colors[i] == -1:
                if not bfs(i):
                    return False

        return True


if __name__ == '__main__':
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(Solution().possibleBipartition(n, dislikes))
