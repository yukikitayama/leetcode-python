"""
sliding window, hashmap
"""

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_i = {}
        ans = 0
        left = 0
        for right in range(len(s)):

            if s[right] in char_to_i:
                # Max because left cannot go back
                left = max(char_to_i[s[right]], left)

            char_to_i[s[right]] = right + 1

            ans = max(ans, right - left + 1)

            # print(f"ans: {ans}, left: {left}, right: {right}")

        return ans

    def lengthOfLongestSubstring1(self, s: str) -> int:

        counter = collections.Counter()
        ans = 0
        left = 0
        for right in range(len(s)):

            while s[right] in counter:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1

            counter[s[right]] += 1

            ans = max(ans, right - left + 1)

        return ans
