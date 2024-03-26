from typing import List
import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        # Get indices of candles
        candles = []
        for i in range(len(s)):
            if s[i] == "|":
                candles.append(i)

        print(candles)

        ans = []

        for left, right in queries:

            print(left, right)

            # Find index for the leftmost candle
            # Leftmost candle is after left
            leftmost_idx = bisect.bisect_left(candles, left)

            # Find index for the rightmost candle
            # Rightmost candle is before right
            rightmost_idx = bisect.bisect_right(candles, right) - 1

            if leftmost_idx < rightmost_idx:
                length_between_candles = candles[rightmost_idx] - candles[leftmost_idx] + 1
                num_candles = rightmost_idx - leftmost_idx + 1
                ans.append(length_between_candles - num_candles)
            else:
                ans.append(0)

        return ans
