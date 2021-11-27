"""
Bottom-up dynamic programming
- dp[i] represents the number of decode ways for substring s[:i],
  from index 0 inclusive to index i exclusive
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        # Base case
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # s starts with s[1] because s[0] was in base case
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            two_digit = int(s[i - 2: i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        # print(f'dp: {dp}')

        return dp[-1]


s = "12"
s = "2326"
s = "06"
print(Solution().numDecodings(s))
