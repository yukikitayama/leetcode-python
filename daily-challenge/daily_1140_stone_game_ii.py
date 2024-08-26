from typing import List
import functools


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = piles[:]
        for i in range(len(piles) - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        @functools.lru_cache(maxsize=None)
        def dp(curr_index, max_till_now):

            # Base case: take all the remaining to finish game,
            # because current index plus twice the max till now exceeds array size
            if curr_index + 2 * max_till_now >= len(piles):
                return suffix_sum[curr_index]

            # res is opponent score we try to minimize
            res = float("inf")
            for i in range(1, 2 * max_till_now + 1):
                res = min(
                    res,
                    dp(curr_index + i, max(i, max_till_now))
                )

            # suffix_sum[curr_index] is what we gain
            # res is what oppornent gains
            return suffix_sum[curr_index] - res

        # print(f"suffix_sum: {suffix_sum}")

        return dp(0, 1)