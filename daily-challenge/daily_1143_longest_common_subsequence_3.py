"""
dp(left, right)
  return
    longest common subsequence up to left and right

if equal,
  move p1 and p2
if not equal,
  move p1
  move p2
  move p1 and p2
"""

import functools


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @functools.cache
        def dp(left, right):

            # Base case
            if left >= len(text1):
                return 0
            if right >= len(text2):
                return 0

            ans = 0

            if text1[left] == text2[right]:
                ans = max(ans, 1 + dp(left + 1, right + 1))
            else:
                ans = max(
                    ans,
                    dp(left + 1, right),
                    dp(left, right + 1),
                    dp(left + 1, right + 1)
                )

            return ans

        return dp(0, 0)


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    # 3

    text1 = "abc"
    text2 = "abc"
    # 3

    text1 = "abc"
    text2 = "def"
    # 0

    print(Solution().longestCommonSubsequence(text1, text2))



