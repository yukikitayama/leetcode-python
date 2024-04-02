"""
recursion
  if left char equal right char
    left + 1
    right - 1
  if left char not equal right char
    left, right - 1
    or left + 1, right
    or left + 1, right - 1

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Bottom-up DP"""
        dp = [[False] * len(s) for _ in range(len(s))]

        # Initialize for the case where given s is length 1 string
        left = 0
        right = 0

        # Base: one character still palindrome
        # Base: 2 characters palindrome
        for i in range(len(s)):
            dp[i][i] = True

            if i != len(s) - 1 and s[i + 1] == s[i]:
                dp[i][i + 1] = True
                left = i
                right = i + 1

        # From 2 to n
        for diff in range(2, len(s)):
            for start in range(0, len(s) - diff):
                end = start + diff
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    left = start
                    right = end

        return s[left:right + 1]

    def longestPalindrome1(self, s: str) -> str:
        """Brute force"""

        def is_palindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # Check from large length to immediately return max length
        for length in range(len(s), 0, -1):
            for left in range(len(s) - length + 1):
                # -1 to be 0-based index
                right = left + length - 1
                if is_palindrome(left, right):
                    return s[left:right + 1]

