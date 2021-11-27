"""
- initialize s index as 0
- Iterate each character in t,
  - if current character == s[index]
    - Increment index
  - Not equal
    - continue
- return index == length(s) - 1
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s is None or len(s) == 0:
            return True

        s_index = 0

        for t_char in t:

            if s_index < len(s) and t_char == s[s_index]:
                s_index += 1

            else:
                continue

        return s_index == len(s)


s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"
s = "b"
t = "abc"
print(Solution().isSubsequence(s, t))
