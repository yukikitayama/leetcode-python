"""
- Time is O(k 2^n)
"""


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total_array_sum = sum(nums)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k
        nums.sort(reverse=True)
        taken = [False] * n

        def backtrack(index, count, curr_sum):
            if count == k - 1:
                return True

            if curr_sum > target_sum:
                return False

            if curr_sum == target_sum:
                # Reset starting index and current sum
                return backtrack(0, count + 1, 0)

            for i in range(index, n):
                if not taken[i]:
                    taken[i] = True
                    if backtrack(i + 1, count, curr_sum + nums[i]):
                        return True
                    taken[i] = False

            return False

        return backtrack(0, 0, 0)




