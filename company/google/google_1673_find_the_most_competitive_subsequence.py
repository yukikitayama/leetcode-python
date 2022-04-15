"""
- heap?
  - Heap is impossible because order will change
"""


from typing import List
import collections


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        additional_count = len(nums) - k

        for i in range(len(nums)):

            # print(f'i: {i}, additional_count: {additional_count}')

            while queue and queue[-1] > nums[i] and additional_count > 0:
                queue.pop()
                additional_count -= 1

            queue.append(nums[i])

        return list(queue)[:k]


if __name__ == '__main__':
    nums = [3, 5, 2, 6]
    k = 2
    nums = [2, 4, 3, 3, 5, 4, 9, 6]
    k = 4
    # [2, 3, 3, 4]
    print(Solution().mostCompetitive(nums, k))
