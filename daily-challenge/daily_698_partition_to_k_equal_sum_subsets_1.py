"""
- get sum
- if sum % k is not 0, return False
- If yes, continue algorithm
- divmod(sum, k) gives us the sum of each subset and remainder to tell us whether it's possible
- initialiaze counter to count how many subsets found so far
- scan from left to right
- keep current value
  - if sum of current value and previous value equal to the quotient, count up
  - if not, keep them as is, go to next
- O(n^2), brute force
"""


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_array_sum = sum(nums)
        n = len(nums)

        target_sum, remainder = divmod(total_array_sum, k)

        if remainder != 0:
            return False

        taken = [False] * n

        def backtrack(count: int, curr_sum: int) -> bool:
            if count == k - 1:
                return True

            if curr_sum > target_sum:
                return False

            if curr_sum == target_sum:
                # Count up the number of subset we have found so far,
                # and reset curr_sum to 0 to start over finding a new subset
                return backtrack(count + 1, 0)

            for j in range(n):
                if not taken[j]:
                    taken[j] = True

                    if backtrack(count, curr_sum + nums[j]):
                        return True

                    # backtrack if the above backtrack was False
                    taken[j] = False

            return False

        return backtrack(0, 0)


"""
TLE
Time: O(n*n!), Space: (n)
"""


nums = [4,3,2,3,5,2,1]
k = 4
print(Solution().canPartitionKSubsets(nums, k))




