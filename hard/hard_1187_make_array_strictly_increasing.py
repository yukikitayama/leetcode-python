from typing import List
import functools
import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        arr2.sort()

        @functools.cache
        def dp(index, prev):

            # Base case: exhausting arr1 so no more operations are needed
            if index == len(arr1):
                return 0

            res = float("inf")

            # State transition

            # Case 1: arr1 is sorted and don't try to find smaller value from arr2
            if arr1[index] > prev:
                res = dp(index + 1, arr1[index])

            # Case 2:
            # Find index of smallest value in arr2 that is greater than prev
            # e.g. arr2: [1, 2, 3, 5], prev: 2, bisect_right: 2, arr2[2]: 3, bisect_left: 1, arr2[1]: 2
            # bisect_right because if arr2 has the same value as prev,
            # we wanna get index after the number in arr2
            i = bisect.bisect_right(arr2, prev)
            if i < len(arr2):
                res = min(
                    res,
                    1 + dp(index + 1, arr2[i])
                )

            return res

        ans = dp(0, -1)

        return -1 if ans == float("inf") else ans