"""
- dp problem?
- scan from left to right
- for each starting index, move the ending index to right
- keep track of current sum, and current length
- when ending index reaches the n - 1,
  - record dp[i] to the max length found so far
  - move the starting index to the left
- find the max length starting from this current starting index
  - dp[i] = max(max_length_found_current, dp[i - 1])
- return dp[len(nums) - 1]
"""


from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = longest_subarray = 0
        prefix_sum_to_index = {}

        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum == k:
                longest_subarray = i + 1

            if prefix_sum - k in prefix_sum_to_index:
                longest_subarray = max(longest_subarray, i - prefix_sum_to_index[prefix_sum - k])

            if prefix_sum not in prefix_sum_to_index:
                prefix_sum_to_index[prefix_sum] = i

        return longest_subarray


"""
Time
Let n be the length of nums. O(n) because one pass

Space:
O(n) for dictionary
"""


nums = [1,-1,5,-2,3]
k = 3
nums = [-2,-1,2,1]
k = 1
print(Solution().maxSubArrayLen(nums, k))

