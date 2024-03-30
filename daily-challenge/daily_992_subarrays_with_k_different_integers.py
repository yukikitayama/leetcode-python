"""
Sliding window
Hashmap or hashset
"""

from typing import List
import collections


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def sliding_window_at_most_k(nums, k):
            counter = collections.Counter()

            left = 0
            ans = 0

            for right in range(len(nums)):

                counter[nums[right]] += 1

                while len(counter) > k:
                    counter[nums[left]] -= 1

                    if counter[nums[left]] == 0:
                        del counter[nums[left]]

                    left += 1

                ans += right - left + 1

            return ans

        ans_k = sliding_window_at_most_k(nums, k)
        ans_k_minus_1 = sliding_window_at_most_k(nums, k - 1)

        return ans_k - ans_k_minus_1
