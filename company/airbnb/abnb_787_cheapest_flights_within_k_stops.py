"""
- Directed, weighted graph
  - Dijkstra's algorithm for weighted graph
    - In Dijkstra, weight is positive
- Use min heap to find cheaper price route
- Time
  - O(nlogk)
"""


from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Make a adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w

        # [print(row) for row in adj_matrix]

        # Shortest distances array
        distances = [float('inf') for _ in range(n)]
        current_stops = [float('inf') for _ in range(n)]
        distances[src] = 0
        current_stops[src] = 0

        # (cost, stops, node)
        min_heap = [(0, 0, src)]

        while min_heap:

            cost, stops, node = heapq.heappop(min_heap)

            if node == dst:
                return cost

            # No more getting neighbors below this block,
            # if stops exceeds at most k stops requirement
            if stops == k + 1:
                continue

            for neighbor in range(n):

                # adjacency matrix contains price.
                # Constraints says price is bigger than or equal to 1
                # so as long as matrix cell is positive, there is a connection
                if adj_matrix[node][neighbor] > 0:

                    total_price_to_curr = cost
                    total_price_to_neighbor = distances[neighbor]
                    price_curr_to_neighbor = adj_matrix[node][neighbor]

                    # If it finds a cheaper total price to the neighbor, update it
                    if total_price_to_curr + price_curr_to_neighbor < total_price_to_neighbor:
                        distances[neighbor] = total_price_to_curr + price_curr_to_neighbor
                        heapq.heappush(min_heap, (
                            total_price_to_curr + price_curr_to_neighbor,
                            stops + 1,
                            neighbor
                        ))

                    # If the total prices is not smaller than the record, but
                    # if the number of stops is smaller, it still pushes it to heap
                    elif stops < current_stops[neighbor]:
                        heapq.heappush(min_heap, (
                            total_price_to_curr + price_curr_to_neighbor,
                            stops + 1,
                            neighbor
                        ))

                    current_stops[neighbor] = stops

        return -1 if distances[dst] == float('inf') else distances[dst]


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))





