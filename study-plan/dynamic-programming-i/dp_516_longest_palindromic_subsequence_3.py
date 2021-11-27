"""
Algorithm, bottom up dp
- Use two pointers, left and right indices
- Left pointer decrements from the last index to the first
- Right pointer increments from the left pointer + 1 to the last index
- dp[i][j] represents the length of the longest palindromic subsequence s[i:j]
- Base case is single character at left and right pointers point at the same character
- If character at left and character at right are the same, it finds a palindrome,
  so move both pointers towards inside and +2 for match
- If characters at left and right are not the same, move either pointer towards inside and take max one of them,
  we add nothing for no match
- Return dp[0][n - 1] because it represents considering from the first index to the last index in s

Complexity
- Time O(mn) for nested for loops
- Space O(mn) for 2d dp array
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):

            # print(f'  i: {i}')

            dp[i][i] = 1

            for j in range(i + 1, n):

                # print(f'    j: {j}')

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # print('dp')
        # [print(row) for row in dp]

        return dp[0][n - 1]


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))

