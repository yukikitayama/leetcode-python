"""
Sliding window
  Contract when num keys is > 2
Hashmap
  k: char
  v: count
"""

import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        left = 0
        counter = collections.Counter()

        for right in range(len(s)):

            counter[s[right]] += 1

            while len(counter.keys()) > 2:
                counter[s[left]] -= 1

                if counter[s[left]] == 0:
                    del counter[s[left]]

                left += 1

            ans = max(ans, right - left + 1)

        return ans
