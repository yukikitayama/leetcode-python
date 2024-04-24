from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_weights = [0] * (len(weights) - 1)

        for i in range(len(weights) - 1):
            pair_weights[i] = weights[i] + weights[i + 1]

        pair_weights.sort()

        ans = 0

        for i in range(k - 1):
            curr_max = pair_weights[len(weights) - 2 - i]
            curr_min = pair_weights[i]

            ans += curr_max - curr_min

            # print(f"i: {i}, curr_max: {curr_max}, curr_min: {curr_min}, ans: {ans}")

        return ans
