"""
curr = 1

[("A", 1), ("B, 2)]

curr: 3
  ("A", 1)
  1 + n = 1 + 2 = 3 is not less than curr
    so curr + 1 = 4
    currr: 5
  ("B", 2)
  2 + n = 2 + 2 = 4 is not less than curr

{"A": 2, "B": 2, "C": 1, "D": 1}
"""

from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0

        while pq:

            # ?
            cycle = n + 1

            store = []

            task_count = 0

            while cycle > 0 and pq:
                current_freq = heapq.heappop(pq)
                current_freq *= -1

                if current_freq > 1:
                    store.append(-(current_freq - 1))

                task_count += 1

                # ?
                cycle -= 1

            for next_freq in store:
                heapq.heappush(pq, next_freq)

            print("  ", pq, task_count, cycle, time, n + 1)

            # ?
            if not pq:
                time += task_count
            else:
                time += (n + 1)

        return time
