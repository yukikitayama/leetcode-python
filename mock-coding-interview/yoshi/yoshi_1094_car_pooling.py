"""
trips: [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
capacity: 23
exp: T

Heap

[[3,2,7],[3,7,9],[8,3,9]]
11
true

[[3,6,9],[10,2,3],[1,6,8],[2,1,6],[9,3,9]]
12
false
"""

from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        t_and_num_pass = []
        for trip in trips:
            # Start time, add num passengers
            t_and_num_pass.append([trip[1], trip[0]])
            # End time, remove num passengers
            t_and_num_pass.append([trip[2], -trip[0]])

        t_and_num_pass.sort()

        print(t_and_num_pass)

        curr_passenger = 0

        for t, num_pass_change in t_and_num_pass:
            curr_passenger += num_pass_change
            if curr_passenger > capacity:
                return False

        return True

    def carPooling2(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2], x[0]))

        # print(trips)

        min_heap = []

        for i in range(len(trips)):

            if not min_heap:
                heapq.heappush(min_heap, (trips[i][2], trips[i][1], trips[i][0]))
                capacity -= trips[i][0]

            # Overlap
            elif trips[i][1] < min_heap[0][0]:
                capacity -= trips[i][0]
                heapq.heappush(min_heap, (trips[i][2], trips[i][1], trips[i][0]))

            # If not overlap
            else:
                while min_heap and trips[i][1] >= min_heap[0][0]:
                    end, start, num_passenger = heapq.heappop(min_heap)
                    capacity += num_passenger
                capacity -= trips[i][0]
                heapq.heappush(min_heap, (trips[i][2], trips[i][1], trips[i][0]))

            if capacity < 0:
                return False

            # print(capacity, min_heap)

        return True

    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2], x[0]))

        print(trips)

        stack = []

        for i in range(len(trips)):

            if not stack:
                stack.append(trips[i])
                capacity -= trips[i][0]

            # Overlap
            elif trips[i][1] < stack[-1][2]:
                capacity -= trips[i][0]
                stack.append(trips[i])

            # If not overlap
            else:
                while stack and trips[i][1] >= stack[-1][2]:
                    num_passenger, start, end = stack.pop()
                    capacity += num_passenger
                stack.append(trips[i])

            if capacity < 0:
                return False

            # print(stack)

        return True
