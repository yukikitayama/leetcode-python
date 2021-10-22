"""
- insert, delete, replace
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # If s and t are the same length, and the current character is different,
                # to be one edit away, the rest of the characters need to be the same
                # By replacing a character, it's one edit away
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]

                # If t is one character longer than s, and the current character is different,
                # to be one edit away, the rest of s including current character and the
                # rest of t excluding the current character need to be the same
                # By deleting a character, it's one edit away
                else:
                    return s[i:] == t[i + 1:]

        # If there's no difference from 0 to up to len(s),
        # if t has one more character, s is one edit away by inserting a character
        return ns + 1 == nt


s = "ab"
t = "acb"
s = ""
t = ""
s = "a"
t = ""
s = ""
t = "A"
print(Solution().isOneEditDistance(s, t))
