"""
- Backtracking
- Each subset has a sum of total array sum / k

- TLE
"""


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_array_sum = sum(nums)
        n = len(nums)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k
        taken = [False] * n

        def backtrack(count, curr_sum):
            if count == k - 1:
                return True

            if curr_sum > target_sum:
                return False

            if curr_sum == target_sum:
                # Reset current sum
                return backtrack(count + 1, 0)

            for i in range(n):
                if not taken[i]:
                    taken[i] = True
                    if backtrack(count, curr_sum + nums[i]):
                        return True
                    taken[i] = False

            return False

        return backtrack(0, 0)






