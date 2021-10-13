"""

"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 2, -1, -1):

            print(f'i: {i}')

            for j in range(i + 1, len(s)):

                print(f'  j: {j}, s[i]: {s[i]}, s[j]: {s[j]}')

                if s[i] == s[j]:
                    memo[i][j] = memo[i + 1][j - 1]

                else:
                    memo[i][j] = 1 + min(
                        memo[i + 1][j],
                        memo[i][j - 1]
                    )

        return memo[0][len(s) - 1] <= k


s = "abcdeca"
k = 2
# s = "abbababa"
# k = 1
print(Solution().isValidPalindrome(s, k))
