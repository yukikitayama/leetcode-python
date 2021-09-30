"""

"""


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total_array_sum = sum(nums)
        target_sum, remainder = divmod(total_array_sum, k)
        if remainder != 0:
            return False

        nums.sort(reverse=True)

        taken = [False] * n

        def backtrack(index, count, curr_sum):
            if count == k - 1:
                return True

            if curr_sum > target_sum:
                return False

            if curr_sum == target_sum:
                return backtrack(0, count + 1, 0)

            for j in range(index, n):
                if not taken[j]:
                    taken[j] = True

                    if backtrack(j + 1, count, curr_sum + nums[j]):
                        return True

                    # Backtrack
                    taken[j] = False

            return False

        return backtrack(0, 0, 0)


"""
Time: O(k*2^n), because we iterate over array k times to get k subsets, hence total time is k
Space: O(n) for boolean array
"""


nums = [4,3,2,3,5,2,1]
k = 4
print(Solution().canPartitionKSubsets(nums, k))




