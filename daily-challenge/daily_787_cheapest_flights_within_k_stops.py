from typing import List
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dist = [float('inf')] * n

        graph = collections.defaultdict(list)
        for from_, to, price in flights:
            graph[from_].append((to, price))

        # print(graph)

        queue = collections.deque([(src, 0)])

        stop = 0

        while queue and stop <= k:

            for _ in range(len(queue)):

                curr, distance = queue.popleft()

                # print(f'curr: {curr}, distance: {distance}')

                for neighbor, p in graph[curr]:

                    # print(f'  neighbor: {neighbor}, p: {p}')

                    if p + distance < dist[neighbor]:
                        dist[neighbor] = p + distance
                        queue.append((neighbor, dist[neighbor]))

            # print(f'dist: {dist}')

            stop += 1

        return dist[dst] if dist[dst] != float('inf') else -1


if __name__ == "__main__":
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    print(Solution().findCheapestPrice(n, flights, src, dst, k))
