"""
two pointers
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p_s = p_t = 0

        while p_s < len(s) and p_t < len(t):

            if s[p_s] == t[p_t]:
                p_s += 1
                p_t += 1

            else:
                p_s += 1

        ans = len(t) - p_t

        return ans
