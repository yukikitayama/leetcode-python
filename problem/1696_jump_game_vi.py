from typing import List
import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = [0] * n
        score[0] = nums[0]
        pq = []
        # Each element: (max score so far, index in array nums)
        heapq.heappush(pq, (-nums[0], 0))

        for i in range(1, n):

            # ?
            while pq[0][1] < i - k:
                print('while')
                heapq.heappop(pq)

            score[i] = nums[i] + score[pq[0][1]]
            heapq.heappush(pq, (-score[i], i))
            print(pq)

        return score[-1]


# nums = [1, -1, -2, 4, -7, 3]
# k = 2
# nums = [10,-5,-2,4,0,3]
# k = 3
nums = [1,-5,-20,4,-1,3,-6,-3]
k = 2
print(f'Answer: {Solution().maxResult(nums, k)}')
