"""
one pass, expand contract sliding window
"""

import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = collections.defaultdict(int)

        left = 0
        right = 0
        ans = 1

        while right < len(s):

            counter[s[right]] = right

            if len(counter.keys()) == 3:

                # Delete leftmost character
                leftmost = min(counter.values())
                del counter[s[leftmost]]
                left = leftmost + 1

            ans = max(right - left + 1, ans)

            right += 1

        return ans


if __name__ == "__main__":
    s = "eceba"
    s = "ccaabbb"
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))
