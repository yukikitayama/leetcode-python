from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # (factor, quality, wage)
        # factor is wage per quality. Because we wanna get the total cost,
        # it's convenient to have wage per quality to get total cost by multiplying with quality
        # sort by factor in ascending order
        workers = sorted([(w / q, q, w) for q, w in zip(quality, wage)])
        # print(f'Tuple: (ratio, quality, wage)')
        # print(f'workers: {workers}')
        # print(f'sorted(workers): {sorted(workers)}')

        ans = float('inf')
        pool = []
        heapq.heapify(pool)
        # sumq is the sum of the heap data structure
        sum_of_quality = 0

        # workers is sorted by ratio in ascending order
        # so we know currently considered worker have the lower ratio, because bigger is coming
        # We increase captain ration in iteration
        for ratio, q, w in workers:
            # print(f'Ratio: {ratio}')

            # -q to make higher quality comes to top to make a max heap
            heapq.heappush(pool, -q)
            sum_of_quality += q

            # We wanna get the smallest k workers in quality
            # so when size of heap is bigger than k, we remove the biggest worker in quality
            if len(pool) > k:
                # max heap contains quality in negative value
                # so here even if it does +=, it's actuall subtracting the sum by the quality amount
                # of the worked just popped out

                # Long story short, pop out highest quality worker and
                # decrease the sum of quality by the worker's quality
                sum_of_quality += heapq.heappop(pool)

            if len(pool) == k:
                # total cost is ratio times the sum of the smallest K workers in quality
                # by smallest k in quality, we can get min cost because we multiply ratio to
                # the sum of the qualities.
                ans = min(ans, ratio * sum_of_quality)

            # print(f'sum_of_quality: {sum_of_quality}, '
            #       f'ratio * sum_of_quality: {ratio * sum_of_quality}, '
            #       f'ans: {ans}')

        return float(ans)


"""
Time complexity
Let n be the number of workers and k is given as the number of workers to be hired, 
O(nlogn) to sort workers and O(logk) to insert and pop from heap data structure
so O(nlogn + logk) = O(nlogn)

Space complexity
O(n) to make a sorted workers list and heap
"""



quality = [10,20,5]
wage = [70,50,30]
k = 2
print(Solution().mincostToHireWorkers(quality, wage, k))
