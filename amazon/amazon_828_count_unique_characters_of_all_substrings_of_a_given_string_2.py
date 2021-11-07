"""
"""


import string


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {c: [-1, -1] for c in string.ascii_uppercase}

        ans = 0

        for i, c in enumerate(s):
            second_last, last = index[c]

            opens = last - second_last
            closes = i - last
            patterns = opens * closes
            ans += patterns
            index[c] = last, i

        for c in index:
            second_last, last = index[c]
            opens = last - second_last
            closes = len(s) - last
            patterns = opens * closes
            ans += patterns

        return ans


s = "ABC"
# s = "ABA"
# s = "LEETCODE"
s = 'XAXAXXAX'
print(Solution().uniqueLetterString(s))
