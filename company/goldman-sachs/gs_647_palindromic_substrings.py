class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        if n <= 0:
            return ans

        # dp[i][j] represents substring starts at i and and ends at j
        dp = [[False] * n for _ in range(n)]

        # Base case
        # Single letter is palindrome
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # Base case
        # Double same letters is palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1

        # e.g. l: 3, i: 0, j: 0 + 3 - 1 = 2, dp[0][2]
        #
        for l in range(3, n + 1):
            i = 0
            j = i + l - 1
            while j < n:
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
                i += 1
                j += 1

        return ans


s = 'abc'
s = "aaa"
print(Solution().countSubstrings(s))
