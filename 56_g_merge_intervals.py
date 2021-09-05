from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort in place
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:

            # If merged is empty or current interval does not overlap with previous
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                right_end = max(merged[-1][1], interval[1])
                merged[-1][1] = right_end

        return merged


"""
Time complexity
O(nlogn) to sort the intervals, O(n) to iterate intervals
O(nlogn) + O(n) = O(nlogn)

Space complexity
O(n) for sorting
"""