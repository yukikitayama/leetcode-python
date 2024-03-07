"""
pwwkew
w: 2,
"""

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        left = 0

        char_to_left = {}

        for right in range(len(s)):

            if s[right] in char_to_left:
                left = max(left, char_to_left[s[right]])

            ans = max(ans, right - left + 1)
            # right + 1 to allow computing lenth 1 answer
            # when we see the same character in further iteration
            char_to_left[s[right]] = right + 1

        return ans

    def lengthOfLongestSubstring1(self, s: str) -> int:
        ans = 0

        left = 0
        char_to_index = collections.defaultdict(int)

        for right in range(len(s)):

            char_to_index[s[right]] += 1

            if len(char_to_index) == right - left + 1:
                ans = max(ans, right - left + 1)
            else:
                char_to_index[s[left]] -= 1
                if char_to_index[s[left]] == 0:
                    del char_to_index[s[left]]
                left += 1

        return ans
