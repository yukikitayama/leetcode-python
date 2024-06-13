"""
Subarray sum
Prefix sum array

nums = [1,5,4,2,9,9,9]
prefix sum: [0, 1, 6, 10, 12, 21, 30, 39]

Sliding window, two pointers
Iterate
  expand window until k
    increment current sum
  when more than k, shrink window
    decrement current sum
Hashmap
  k: num
  v: count
  if length of hashmap is k
    the window is valid

[1, 5, 4]
  {1: 1, 5: 1, 4: 1}, len: 3 == k
[2, 9, 9]
  {2: 1, 9: 2}, len: 2 != k,

T: O(N)
S: O(k)

Subarray
Subsequence
"""

from typing import List
import collections


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        curr_sum = 0
        ans = 0

        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            counter[nums[right]] += 1

            if right - left + 1 > k:
                curr_sum -= nums[left]
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1

            if len(counter) == k:
                ans = max(ans, curr_sum)

        return ans



