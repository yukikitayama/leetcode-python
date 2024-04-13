"""
two pointers sliding window

nums = [1,4,3,3,2]
subarray [1,4,3,3,2], with its largest element 1. The first element is 1 and the last element is also 1.
subarray [1,4,3,3,2], with its largest element 4. The first element is 4 and the last element is also 4.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 2. The first element is 2 and the last element is also 2.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
"""

from typing import List
import heapq


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:

        # [(num, count)], monotonically decreasing
        stack = []

        ans = 0

        for i in range(len(nums)):

            while stack and stack[-1][0] < nums[i]:
                stack.pop()

            if not stack or stack[-1][0] > nums[i]:
                stack.append([nums[i], 0])

            stack[-1][1] += 1

            ans += stack[-1][1]

            # print(f"i: {i}, ans: {ans}, stack: {stack}")

        return ans

    def numberOfSubarrays1(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        max_heap = []
        heapq.heapify(max_heap)

        for right in range(len(nums)):

            heapq.heappush(max_heap, -nums[right])

            while max_heap and left < right and nums[left] != -max_heap[0] or nums[right] != -max_heap[0]:
                if nums[left] == -max_heap[0]:
                    heapq.heappop(max_heap)
                left += 1

            if nums[left] == -max_heap[0] and nums[right] == -max_heap[0]:
                ans += right - left + 1

            print(f"right: {right}, left: {left}, max_heap: {max_heap}, ans: {ans}")

        return ans
