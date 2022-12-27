from typing import List
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        # Min heap
        heapq.heapify(sticks)

        ans = 0

        while len(sticks) > 1:

            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)

            cost = a + b
            ans += cost

            heapq.heappush(sticks, cost)

        return ans


if __name__ == '__main__':
    sticks = [2, 4, 3]
    sticks = [1, 8, 3, 5]
    print(Solution().connectSticks(sticks))



