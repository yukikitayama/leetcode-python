from typing import List
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        candidates = zip(efficiency, speed)

        # Sort by efficiency in a descending order
        # candidates = (
        #     [high efficiency, ..., low efficiency],
        #     [first person speed, ..., last person speed]
        # )
        candidates = sorted(candidates, key=lambda t: t[0], reverse=True)

        speed_heap = []
        speed_sum = 0
        perf = 0

        for curr_efficiency, curr_speed in candidates:
            print(f'curr_efficiency: {curr_efficiency}, curr_speed: {curr_speed}')

            if len(speed_heap) > k - 1:
                # heappop removes and returns the smallest element
                tmp = heapq.heappop(speed_heap)
                speed_sum -= tmp
                print(f'heappoped: {tmp}')

            # From high efficiency person, speed goes to the heap
            heapq.heappush(speed_heap, curr_speed)

            speed_sum += curr_speed

            perf = max(perf, speed_sum * curr_efficiency)

        return perf % (10 ** 9 + 7)


n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
# k = 3
sol = Solution()
answer = sol.maxPerformance(n=n, speed=speed, efficiency=efficiency, k=k)
print(f'Answer: {answer}')
