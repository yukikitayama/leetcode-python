"""
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """DP
        If dp[i][j] is true, s[i:j + 1] is palindrome
        """
        start = 0
        end = 0
        dp = [[False] * len(s) for _ in range(len(s))]

        # Base case: odd legnth
        for i in range(len(s)):
            dp[i][i] = True

        # Base case: even length
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                end = i + 1

        # Recurrence transition
        for diff in range(2, len(s)):
            for left in range(0, len(s) - diff):
                right = left + diff
                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    # diff incrementally gets bigger, so last recorded start and end can maximize the subarray length
                    start = left
                    end = right

        return s[start:end + 1]

    def longestPalindrome1(self, s: str) -> str:
        """Expand from center"""

        start = 0
        end = 0

        for i in range(len(s)):
            # i: odd length palindrome
            # i + 1: even length palindrome
            for j in [i, i + 1]:

                left = i
                right = j
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                # Here, different character, so go back
                left += 1
                right -= 1

                if right - left > end - start:
                    start = left
                    end = right

        return s[start:end + 1]

