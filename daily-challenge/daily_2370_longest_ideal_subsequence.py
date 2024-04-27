"""
10,000,000,000
"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26

        ans = 0

        for i in range(n):

            curr = ord(s[i]) - ord("a")

            max_so_far = 0
            for prev in range(26):
                if abs(prev - curr) <= k:
                    max_so_far = max(max_so_far, dp[prev])

            dp[curr] = max(dp[curr], max_so_far + 1)

            ans = max(ans, dp[curr])

            # print(dp)

        return ans

    def longestIdealString2(self, s: str, k: int) -> int:
        n = len(s)

        dp = [[-1] * 26 for _ in range(n)]

        def dfs(i, c, dp, s, k):

            # If memoization performed previously, return the cached result
            if dp[i][c] != -1:
                return dp[i][c]

            # Base case
            dp[i][c] = 0
            match = c == (ord(s[i]) - ord("a"))
            if match:
                dp[i][c] = 1

            # State transition
            if i > 0:
                dp[i][c] = dfs(i - 1, c, dp, s, k)

                if match:
                    for p in range(26):
                        if abs(c - p) <= k:
                            dp[i][c] = max(
                                dp[i][c],
                                1 + dfs(i - 1, p, dp, s, k)
                            )

            return dp[i][c]

        ans = 0
        for c in range(26):
            ans = max(ans, dfs(n - 1, c, dp, s, k))
        return ans

    def longestIdealString1(self, s: str, k: int) -> int:

        # for ch in s:
        #     print(ord(ch))

        dp = [1] * len(s)

        for right in range(1, len(s)):
            for left in range(right):
                if abs(ord(s[right]) - ord(s[left])) <= k:
                    dp[right] = max(
                        1 + dp[left],
                        dp[right]
                    )

        # print(dp)

        return max(dp)