"""
- Initialize left to 0 and right to len(s) - 1
- while left < right
  - put s[left] to s[right] and s[right] to s[left]
"""


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        print(f's: {s}')

        while left < right:

            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1

        print(f's: {s}')


"""
- Time is O(n)
- Space is O(1)
"""


s = ["h", "e", "l", "l", "o"]
s = ["H","a","n","n","a","h"]
print(Solution().reverseString(s))
