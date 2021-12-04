"""
- Bellman-Ford algorithm
  - Use two arrays, previous and current
"""


from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        previous = [float('inf')] * n
        current = [float('inf')] * n
        previous[src] = 0

        # +2 because at most k stop means at most k + 1 edges.
        # and we want k + 1 to be included, so k + 2 exclusive end in range()
        for i in range(1, k + 2):
            current[src] = 0
            for flight in flights:
                previous_flight, current_flight, cost = flight
                if previous[previous_flight] < float('inf'):
                    current[current_flight] = min(current[current_flight], previous[previous_flight] + cost)

            # current.copy() also is fine
            # make sure not assign the reference
            previous = current[:]

        return current[dst] if current[dst] != float('inf') else -1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))

