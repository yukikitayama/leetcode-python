from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        wage_to_quality_quality = []
        for i in range(len(quality)):
            wage_to_quality_quality.append([
                wage[i] / quality[i],
                quality[i]
            ])
        wage_to_quality_quality.sort()

        max_heap = []
        ans = float("inf")
        curr_total_quality = 0
        for i in range(len(quality)):
            # Push quality
            heapq.heappush(max_heap, -wage_to_quality_quality[i][1])

            curr_total_quality += wage_to_quality_quality[i][1]

            if len(max_heap) > k:
                q = heapq.heappop(max_heap)
                q *= -1
                curr_total_quality -= q

            if len(max_heap) == k:
                ans = min(
                    ans,
                    curr_total_quality * wage_to_quality_quality[i][0]
                )

        return ans