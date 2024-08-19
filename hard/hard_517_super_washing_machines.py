"""
sum should be divisible by length of machines array
greedy
  move highest to adjacent
"""

from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        dress_per_machine, remainder = divmod(sum(machines), len(machines))

        if remainder != 0:
            return -1

        # Normalize
        for i in range(len(machines)):
            machines[i] -= dress_per_machine

        print(f"machines: {machines}")

        curr_sum = 0
        max_sum = 0
        ans = 0

        for m in machines:
            curr_sum += m

            max_sum = max(
                max_sum,
                # abs to receive from left to curr
                abs(curr_sum)
            )

            ans = max(
                ans,
                max_sum,
                m
            )

            # print(f"m: {m}, curr_sum: {curr_sum}, max_sum: {max_sum}, ans: {ans}")

        return ans
