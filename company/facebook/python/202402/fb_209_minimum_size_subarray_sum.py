"""
target: 7
nums: [2,3,1,2,4,3]
[0, 2, 5, 6, 8, 12, 15]

hashmap
  k: prefix sum
  v: index, will updated to recent index

If current prefix sum - target exist
  current index - previous index is the length
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """The constraints say that numbers are more than 0, so
        the prefix sum array are guaranteed to increase,
        so we can use two pointers and expand if current sum is smaller,
        and shrink if current sum is greater than target.
        """
        ans = float("inf")

        left = 0
        curr_sum = 0

        for right in range(len(nums)):

            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans, right - left + 1)

                curr_sum -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        prefix_sums = [0]

        for i in range(len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])

        ans = float("inf")

        for i in range(len(prefix_sums)):
            for j in range(i, len(prefix_sums)):
                sum_ = prefix_sums[j] - prefix_sums[i]

                if sum_ >= target:
                    ans = min(ans, j - i)

                    # Can break the most inner for-loop because
                    # i and j starts with the closest distance, and
                    # we want the minimal length
                    break

        return 0 if ans == float("inf") else ans

    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        ans = float("inf")

        prefix_sum = 0
        prefix_sum_to_index = {prefix_sum: -1}

        for i in range(len(nums)):

            prefix_sum += nums[i]

            if prefix_sum - target in prefix_sum_to_index:
                ans = min(ans, i - prefix_sum_to_index[prefix_sum - target])

            prefix_sum_to_index[prefix_sum] = i

        return 0 if ans == float("inf") else ans
