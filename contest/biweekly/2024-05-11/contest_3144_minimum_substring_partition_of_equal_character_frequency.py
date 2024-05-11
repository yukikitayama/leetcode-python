"""
dp(i, char)
  return the min number of substring from left to ith

Input: s = "fabccddg"

Output: 3
Return the minimum number of substrings that you can partition s into.

Explanation:
We can partition the string s into 3 substrings in one of the following ways: ("fab, "ccdd", "g"), or ("fabc", "cd", "dg").
"""

import collections
import functools


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:

        @functools.cache
        def dp(index):

            # Base case
            if index >= len(s):
                return 0

            curr_counter = collections.Counter()

            ans = float("inf")

            for i in range(index, len(s)):
                curr_counter[s[i]] += 1

                if len(set(curr_counter.values())) == 1:
                    ans = min(
                        ans,
                        1 + dp(i + 1)
                    )

            return ans

        return dp(0)