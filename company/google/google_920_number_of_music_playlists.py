"""
- DP
- backtracking
"""


from functools import lru_cache


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        # dp[i][j]: i length playlist with j unique songs
        # We want dp[goal][n]
        @lru_cache(None)
        def dp(i, j):

            if i == 0:
                return int(j == 0)

            # Last song was a new song
            # Listened i - 1 songs with j - 1 unique songs
            # The new song was N - (j - 1) songs, because (j - 1) songs were already listened
            ans = dp(i - 1, j - 1) * (n - (j - 1))

            # Last song was an old song which already listened
            # We repeated the previous same song, so j
            # If j <= k, it will be 0 because only after choosing k different other songs,
            # then old song can be chosen
            ans += dp(i - 1, j) * max(j - k, 0)

            return ans % (10**9 + 7)

        return dp(goal, n)


if __name__ == '__main__':
    n = 3
    goal = 3
    k = 1
    print(Solution().numMusicPlaylists(n, goal, k))
