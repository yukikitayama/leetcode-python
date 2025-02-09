"""
https://leetcode.com/problems/find-longest-self-contained-substring/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days
"""

import collections
import bisect


class Solution:
    def maxSubstringLength(self, s: str) -> int:

        char_to_indices = collections.defaultdict(list)
        for i, char in enumerate(s):
            char_to_indices[char].append(i)

        print(char_to_indices)

        def check(l, r):
            for k in char_to_indices:
                # Left most
                x = bisect.bisect_left(char_to_indices[k], l)
                # Comes after
                y = bisect.bisect_right(char_to_indices[k], r)

                # ?
                if not (y - x == len(char_to_indices[k]) or x == y):
                    return False

            return True

        ans = -1

        for k1 in char_to_indices:

            # First occurance as left bound
            a = char_to_indices[k1][0]

            for k2 in char_to_indices:

                # Last occurance as right bound
                b = char_to_indices[k2][-1]

                # Invalid case
                if (a > b) or (b - a + 1 == len(s)):
                    continue

                # If valid
                if check(a, b):
                    ans = max(ans, b - a + 1)

        return ans