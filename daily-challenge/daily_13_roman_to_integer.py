"""
- integer division to make the current number smaller and get the biggest number
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        i = 0

        while i < len(s):

            if i + 1 < len(s) and roman_to_integer[s[i]] < roman_to_integer[s[i + 1]]:
                ans += roman_to_integer[s[i + 1]] - roman_to_integer[s[i]]
                i += 2

            else:
                ans += roman_to_integer[s[i]]
                i += 1

        return ans

