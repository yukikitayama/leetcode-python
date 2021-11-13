"""
- Two pointers left and right
  - If substring does not contain all in t, increment right pointer
  - If substring contains all of the
"""


import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = collections.Counter(t)
        left = right = 0
        dict_s = collections.defaultdict(int)

        formed = 0

        ans = (float('inf'), left, right)

        while right < len(s):
            curr_char = s[right]
            dict_s[curr_char] += 1

            if curr_char in dict_t and dict_s[curr_char] == dict_t[curr_char]:
                formed += 1

            # Contract
            while left <= right and formed == len(dict_t):

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                curr_char_left = s[left]
                dict_s[curr_char_left] -= 1
                if curr_char_left in dict_t and dict_s[curr_char_left] < dict_t[curr_char_left]:
                    formed -= 1
                left += 1

            # Expand
            right += 1

        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+ 1]


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))


