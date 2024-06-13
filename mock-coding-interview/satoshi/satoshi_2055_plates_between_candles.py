"""
for each query
  get substring from s
    two pointers
      left pointer search first canfle from left
      right pointer search first candle from right
      keep

N: s length
M: length of queries array
T: O(M*N) = 10**10
"""

from typing import List
import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_positions = []
        for i in range(len(s)):
            if s[i] == "|":
                candle_positions.append(i)

        ans = []

        for left, right in queries:

            # Works even if overlap
            l = bisect.bisect_left(candle_positions, left)
            # -1 because it goes out of bound
            # e.g. [1, 2, 3], right: 4, bisect: 3 - 1 = 2
            # e.g. [1, 2, 3], right: 3, bisect: 3 - 1 = 2
            # e.g. [1, 2, 4], right: 3, bisect: 2 - 1 = 1
            r = bisect.bisect_right(candle_positions, right) - 1

            if l < r:
                # Inclusive length
                # candle_positions: [1, 3, 5], l: 1, r: 2, len: 5 - 3 + 1
                length = candle_positions[r] - candle_positions[l] + 1
                # Inclusive
                num_candles = r - l + 1
                ans.append(length - num_candles)
            else:
                ans.append(0)

        return ans

    def platesBetweenCandles1(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []

        def count_plates(l, r):
            left_found = right_found = False
            while l < r and (not left_found or not right_found):
                if s[l] == "|":
                    left_found = True
                l += 1

                if s[r] == "|":
                    right_found = True
                r -= 1

            # print(l, r, left_found, right_found)

            num_plates = 0
            if left_found and right_found:
                while l <= r:
                    if s[l] == "*":
                        num_plates += 1
                    l += 1
                return num_plates
            else:
                return num_plates

        for query in queries:
            num_plates = count_plates(query[0], query[1])
            ans.append(num_plates)

        return ans
