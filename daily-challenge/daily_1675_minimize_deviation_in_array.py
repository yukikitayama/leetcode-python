from typing import List
import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_ = float('inf')

        for num in nums:

            if num % 2 == 0:
                heapq.heappush(max_heap, -num)
                min_ = min(min_, num)

            else:
                heapq.heappush(max_heap, -num * 2)
                min_ = min(min_, num * 2)

        ans = float('inf')

        while max_heap:

            curr = -heapq.heappop(max_heap)
            ans = min(ans, curr - min_)
            if curr % 2 == 0:
                min_ = min(min_, curr // 2)
                heapq.heappush(max_heap, -curr // 2)

            # If max is odd, end
            else:
                break

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().minimumDeviation(nums))
