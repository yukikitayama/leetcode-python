"""
Brute force
  T: O(3 ** n)
    for each rod, 3 choices for being used for 1st stand, used for 2nd stand, or not used
"""

from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for rod in rods:

            # dp is case where current rod not used
            # Also work as previous dp
            new_dp = dp.copy()

            # dp.items() means previous dp
            for diff, taller in dp.items():
                shorter = taller - diff

                # Add current rod to taller
                new_dp[diff + rod] = max(
                    taller + rod,
                    new_dp.get(diff + rod, 0)
                )

                # Add current rod to shorter
                shorter_plus_rod = shorter + rod
                new_diff = abs(shorter_plus_rod - taller)
                new_height = max(taller, shorter_plus_rod)
                new_dp[new_diff] = max(
                    new_dp.get(new_diff, 0),
                    new_height
                )

            dp = new_dp

        return dp[0]

    def tallestBillboard1(self, rods: List[int]) -> int:

        def helper(half_rods):
            states = set()
            # No rods added
            states.add((0, 0))

            for curr_rod in half_rods:
                new_states = set()

                for left, right in states:
                    updated_left = left + curr_rod
                    updated_right = right + curr_rod
                    # Save current combination
                    new_states.add((updated_left, right))
                    new_states.add((left, updated_right))

                # Save total combination
                states |= new_states  # Union

            diff_to_left = {}
            for left, right in states:
                diff_to_left[left - right] = max(
                    left,
                    diff_to_left.get(left - right, 0)
                )

            return diff_to_left

        n = len(rods)
        first_half = helper(rods[:n // 2])
        second_half = helper(rods[n // 2:])

        ans = 0

        for diff in first_half:
            if -diff in second_half:
                ans = max(
                    ans,
                    first_half[diff] + second_half[-diff]
                )

        return ans
