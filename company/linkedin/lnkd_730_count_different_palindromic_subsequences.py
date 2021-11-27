class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)

        # dp[i][j] represents from i to j both inclusive number of palindromic subsequences
        dp = [[0] * n for _ in range(n)]

        # Base case
        for i in range(n):
            dp[i][i] = 1

        # [print(row) for row in dp]

        # distance gives us all the possible starting i and ending j combinations
        for distance in range(1, n):

            # i gives us the starting
            for i in range(n - distance):

                # j gives us the ending
                j = i + distance

                # print(f'  i: {i}, j: {j}, distance: {distance}, '
                #       f's[i]: {s[i]}, s[j]: {s[j]}')

                if s[i] == s[j]:
                    # ?
                    # low and high are used to get rid of the duplicate?
                    low = i + 1
                    high = j - 1

                    while low <= high and s[low] != s[j]:
                        low += 1

                    while low <= high and s[high] != s[j]:
                        high -= 1

                    if low > high:
                        # ?
                        # a...a
                        # e.g. s: aba, i: 0, j: 2, dp[1][1]: b,
                        # dp[i + 1][j - 1] * 2 because b and aba
                        # + 2 because a and aa
                        # in total a, b, aa, aba
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2

                    elif low == high:
                        # ?
                        # a...a...a
                        # e.g. s: aaa, i: 0, j: 2, dp[i + 1][j - 1]: a,
                        # dp[i + 1][j - 1] * 2 because a and aaa
                        # + 1 because aa of s[i] + s[j]
                        # in total, a, aa, aaa
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1

                    else:
                        # ?
                        # a...a...a...a
                        # e.g. s: aacaa, i: 0, j: 4, dp[i + 1][j - 1]: a, c, aa, aca
                        # dp[i + 1][j - 1] * 2 because one time as {a, c, aa, aca}
                        # and second time as {aaa, aca, aaaa, aacaa}
                        # -dp[low + 1][high - 1] because aca is duplicate above
                        # in total, a, c, aa, aca, aaa, aaaa, aacaa
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]

                else:
                    # ?
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]

                dp[i][j] = dp[i][j] + 10**9 + 7 if dp[i][j] < 0 else dp[i][j] % (10**9 + 7)

        return dp[0][n - 1]


s = 'bccb'
s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"  # 104860361
print(Solution().countPalindromicSubsequences(s))


