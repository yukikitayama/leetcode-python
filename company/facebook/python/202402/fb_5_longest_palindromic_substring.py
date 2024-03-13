"""
Two pointers
  left and right, move towards center
  if two characters are the same,
    move both pointers
  if two characters are different
    move left
    move right
    or move both
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            """Returns length of palindrome"""

            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # -1 because when breaking while loop, it's longer than what we want
            # cabad, right: 4, left: 0, 4 - 0 - 1 = 3
            return right - left - 1

        left = 0
        right = 0

        for i in range(len(s)):

            # Odd length
            odd_length = expand(i, i)
            # If found longer palindrome
            if odd_length > right - left + 1:
                distance = odd_length // 2
                left = i - distance
                right = i + distance

            # Even length
            even_length = expand(i, i + 1)

            if even_length > right - left + 1:
                distance = even_length // 2 - 1
                left = i - distance
                right = (i + 1) + distance

        return s[left:right + 1]

    def longestPalindrome1(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]

        # Base case: one character is still a palindrome
        for i in range(len(s)):
            dp[i][i] = True

        left = 0
        right = 0

        # Base case: even length
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                left = i
                right = i + 1

        # 2: 3 length substring, len(s) - 1: entire string
        for diff in range(2, len(s)):

            for l in range(len(s) - diff):

                r = l + diff

                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    left = l
                    right = r

        return s[left:right + 1]

