import functools


class Solution:
    def knightDialer(self, n: int) -> int:

        # Array index as pad key and each element as list of next pads
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4],
        ]

        @functools.cache
        def dp(remain, source_number):

            if remain == 0:
                return 1

            ans = 0

            for next_number in jumps[source_number]:
                ans = (ans + dp(remain - 1, next_number)) % (10 ** 9 + 7)

            return ans

        ans = 0
        for source_number in range(10):
            ans = (ans + dp(n - 1, source_number)) % (10 ** 9 + 7)

        return ans


class SolutionBottomUp:
    def knightDialer(self, n: int) -> int:

        # Array index as pad key and each element as list of next pads
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4],
        ]

        # dp = [[0] * 10 for _ in range(n + 1)]
        dp = [[0] * 10 for _ in range(n)]
        for square in range(10):
            dp[0][square] = 1

        for remain in range(1, n):
            for square in range(10):
                ans = 0
                for next_square in jumps[square]:
                    ans = (ans + dp[remain - 1][next_square]) % (10 ** 9 + 7)
                dp[remain][square] = ans

        # [print(row) for row in dp]

        ans = 0
        for square in range(10):
            ans = (ans + dp[n - 1][square]) % (10 ** 9 + 7)
        return ans


if __name__ == "__main__":
    n = 2
    print(SolutionBottomUp().knightDialer(n))
