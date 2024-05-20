"""
Largest range is min of k arrays to max of k arrays
  Shrink this range towards center as long as it's valid
"""

from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # [(val, row, col)]
        min_heap = []
        max_val = float("-inf")
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        ans = [min_heap[0][0], max_val]

        while True:

            val, r, c = heapq.heappop(min_heap)

            # len - 1 to avoid index out of bound below nums access
            if c == len(nums[r]) - 1:
                break

            heapq.heappush(min_heap, (nums[r][c + 1], r, c + 1))
            max_val = max(max_val, nums[r][c + 1])

            if ans[1] - ans[0] > max_val - min_heap[0][0]:
                ans[0] = min_heap[0][0]
                ans[1] = max_val

        return ans

    def smallestRange2(self, nums: List[List[int]]) -> List[int]:

        # [(val, index to nums)]
        min_heap = []
        curr_max = float("-inf")
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i))
            curr_max = max(curr_max, nums[i][0])

        # print(f"min_heap: {min_heap}, curr_max: {curr_max}")

        max_val = float("inf")
        min_val = float("-inf")
        next_ = [0] * len(nums)
        exhausted = False

        i = 0
        while not exhausted and i < len(nums):

            j = 0
            while not exhausted and j < len(nums[i]):

                curr_min, min_k = heapq.heappop(min_heap)

                # print(f"curr_min: {curr_min}, min_k: {min_k}")

                if max_val - min_val > curr_max - nums[min_k][next_[min_k]]:
                    min_val = nums[min_k][next_[min_k]]
                    max_val = curr_max

                # print(f"[min_val, max_val]: {[min_val, max_val]}")

                next_[min_k] += 1

                if next_[min_k] == len(nums[min_k]):
                    exhausted = True
                    break

                heapq.heappush(min_heap, (nums[min_k][next_[min_k]], min_k))
                curr_max = max(curr_max, nums[min_k][next_[min_k]])

                # print(f"min_heap: {min_heap}, curr_max: {curr_max}")

                j += 1

            i += 1

        return [min_val, max_val]

    def smallestRange1(self, nums: List[List[int]]) -> List[int]:
        min_val = float("-inf")
        max_val = float("inf")

        exhausted = False

        next_ = [0] * len(nums)

        i = 0
        while not exhausted and i < len(nums):

            j = 0
            while not exhausted and j < len(nums[i]):

                curr_min_i = 0
                curr_max_i = 0

                for k in range(len(nums)):

                    if nums[curr_min_i][next_[curr_min_i]] > nums[k][next_[k]]:
                        curr_min_i = k

                    if nums[curr_max_i][next_[curr_max_i]] < nums[k][next_[k]]:
                        curr_max_i = k

                if max_val - min_val > nums[curr_max_i][next_[curr_max_i]] - nums[curr_min_i][next_[curr_min_i]]:
                    min_val = nums[curr_min_i][next_[curr_min_i]]
                    max_val = nums[curr_max_i][next_[curr_max_i]]

                next_[curr_min_i] += 1

                if next_[curr_min_i] == len(nums[curr_min_i]):
                    exhausted = True

                j += 1

            i += 1

        return [min_val, max_val]