"""
- (1, 1)
  - (0, 1) + (1, 0)
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:

        memo = [[0] * 6 for _ in range(n + 1)]

        def count_vowel_strings(n, vowels):

            if n == 1:
                return vowels

            if vowels == 1:
                return 1

            if memo[n][vowels] != 0:
                return memo[n][vowels]

            ans = count_vowel_strings(n - 1, vowels) + count_vowel_strings(n, vowels - 1)

            memo[n][vowels] = ans

            return ans

        return count_vowel_strings(n, 5)


if __name__ == '__main__':
    n = 2
    print(Solution().countVowelStrings(n))
