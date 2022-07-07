"""
- two pointers?
- Overlapping subproblem
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True

                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])

                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])

                else:
                    dp[i][j] = (dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])) or (dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1]))

        return dp[-1][-1]


class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memo = [[-1] * len(s2) for _ in range(len(s1))]

        def is_interleave(i, j, k):
            if i == len(s1):
                return s2[j:] == s3[k:]

            if j == len(s2):
                return s1[i:] == s3[k:]

            if memo[i][j] >= 0:
                return True if memo[i][j] == 1 else False

            ans = False
            if (
                (s1[i] == s3[k] and is_interleave(i + 1, j, k + 1))
                or (s2[j] == s3[k] and is_interleave(i, j + 1, k + 1))
            ):
                ans = True

            memo[i][j] = 1 if ans else 0

            return ans

        if len(s1) + len(s2) != len(s3):
            return False

        return is_interleave(0, 0, 0)


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # true
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    # false
    s1 = "aaaa"
    s2 = "aa"
    s3 = "aaa"
    # false
    print(Solution().isInterleave(s1, s2, s3))
