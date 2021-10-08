"""
- use iter
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(char in it for char in s)


s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"
print(Solution().isSubsequnce(s, t))
