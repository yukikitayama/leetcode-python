"""
Sort start indices
  Binary search with target end

[1, 2, 3]
  target
    4,
    3,
    2
"""

from typing import List
import collections


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_to_index = collections.defaultdict(int)
        starts = []

        for i in range(len(intervals)):
            start_to_index[intervals[i][0]] = i
            starts.append(intervals[i][0])

        starts.sort()

        # print(start_to_index)
        # print(starts)

        def binary_search(target):
            left = 0
            right = len(starts) - 1

            while left <= right:
                mid = (left + right) // 2

                if starts[mid] == target:
                    return mid

                elif starts[mid] < target:
                    left = mid + 1

                elif starts[mid] > target:
                    right = mid - 1

            # When target doesn't exist in the array,
            # but left insertion point is within array length
            if left < len(starts):
                return left
            # When target doesn't exist in the array
            # and the target is bigger than any numbers in the array
            else:
                return -1

        ans = []

        for i in range(len(intervals)):

            end = intervals[i][1]

            # Find the smallest start number which is greater than or equal to the above end
            res = binary_search(end)

            if res == -1:
                ans.append(-1)
            else:
                start = starts[res]
                index = start_to_index[start]
                ans.append(index)

            # print(f"end: {end}, res: {res}")

        return ans
