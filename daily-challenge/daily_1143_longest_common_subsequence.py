"""
dp[i] represents the length of the longest common subsequence up to index of i
dp[0] has a base case 0. dp length is
dp should be 2d
- text1: row, text2: col

text1: abcde, text2: ace

e 0
d 0
c 0    1    2
b 0    1    1
a 0    1    1
_ 0    0    0    0
  _    a    c    e

b    0    1    2
a    0    1    1
_    0    0    0
     _    a    b
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    # no plus 1 to dp[i - 1][j] and dp[i][j - 1] because it's going back and double count
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        # [print(row) for row in dp]

        return dp[len(dp) - 1][len(dp[0]) - 1]


text1 = "abcde"
text2 = "ace"
text1 = "abc"
text2 = "def"
text1 = "bsbininm"  # b at 2,
text2 = "jmjkbkjkv"  # b at 4
# it's going back
print(Solution().longestCommonSubsequence(text1, text2))

