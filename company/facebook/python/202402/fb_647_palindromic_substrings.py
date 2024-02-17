"""
abcba
  if abcba is palindrome, bcb is also palindrome, and c is also palindrome
  when we have bcb
    add left
    add right
    add both

dp(left, right)
  base: odd
    when left == right
      return 1
  base: even
    when left + 1 == right and left character and right character are the same
      return 1
  palindrome if
    first and last characters are the same
    the inside characters are palindrome
  dp(left, right) is true if dp(left + 1, right - 1) is true, and if left character and right character are the same


Expand from a center towards both ends
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand(left, right):
            ans = 0
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break

                ans += 1
                left -= 1
                right += 1
            return ans

        ans = 0

        # For each center, expand
        for i in range(len(s)):
            # Odd length
            ans += expand(i, i)

            # Even length
            ans += expand(i, i + 1)

        return ans

        return ans

