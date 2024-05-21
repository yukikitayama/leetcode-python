"""
dp(i)
  return number of ways for the first i digits
  base case
    if i is equal to 0, return 1
    if i < 0, return 0
  state transition
    include current digit
      if "0", cannot include
    or include current plus next digit
      if "0X", cannot include
      if more than "26", cannot include
    ans = 0
    ans += dp(i - 1)
    ans += dp(i - 2)
Return dp(s length - 1)

"2611055971756562"
exp: 4
"""

import functools


class Solution:
    def numDecodings(self, s: str) -> int:
        """Bottom-up DP, S: O(1)"""

        prev1 = 1
        prev2 = 0
        curr = 0

        for i in range(len(s)):

            # 1 digit
            if s[i] != "0":
                curr += prev1

            # 2 digits
            if i - 1 >= 0:
                if (
                    (s[i - 1] == "1" and s[i] in "0123456789")
                    or (s[i - 1] == "2" and s[i] in "0123456")
                ):
                    curr += prev2

            prev2 = prev1
            prev1 = curr

        return curr

    def numDecodings(self, s: str) -> int:
        """Bottom-up DP, S: O(N)"""
        dp = [0] * (len(s) + 1)

        # Base case
        dp[0] = 1

        for i in range(len(s)):

            # 1 digit
            if s[i] != "0":
                dp[i + 1] += dp[i]

            # 2 digits
            if i - 1 >= 0:
                if (
                    (s[i - 1] == "1" and s[i] in "0123456789")
                    or (s[i - 1] == "2" and s[i] in "0123456")
                ):
                    dp[i + 1] += dp[i - 1]

        # print(dp)

        return dp[-1]

    def numDecodings1(self, s: str) -> int:
        """Top-down DP"""

        @functools.cache
        def dp(index):

            if index == len(s):
                return 1
            elif index > len(s):
                return 0

            ans = 0

            # 1 digit
            if s[index] != "0":
                ans += dp(index + 1)

            # 2 digits
            if index + 1 < len(s):
                if (
                    (s[index] == "1" and s[index + 1] in "0123456789")
                    or (s[index] == "2" and s[index + 1] in "0123456")
                ):
                    ans += dp(index + 2)

            return ans

        return dp(0)