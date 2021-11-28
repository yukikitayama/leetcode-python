class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def uniqueSubsequences(i, j):
            M, N = len(s), len(t)

            # Third condition checks remaining characters in s is enough to make a subsequence for t
            # e.g. M: 7, N: 6, i: 5, j: 2
            # (7 - 5) < (6 - 2) = 2 < 4 = T, int(2 == N): int(2 == 6) = int(False) = 0
            if i == M or j == N or M - i < N - j:

                # print(f'Base case return, i: {i}, j: {j}')
                # print(f'Base case return, s[i]: {s[i]}, t[j]: {t[j]}')

                return int(j == N)

            if (i, j) in memo:
                return memo[i, j]

            ans = uniqueSubsequences(i + 1, j)

            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)

            # Memoization or caching
            # When you put two items to key with comma, key will be a tuple of (i, j)
            memo[i, j] = ans

            # print(f'Final return, s[i]: {s[i]}, t[j]: {t[j]}')

            return ans

        return uniqueSubsequences(0, 0)


"""
Time complexity
Let m be the length of s, and n be the length of t.
Single call of uniqueSubsequences() takes O(i).
But we have recursive times call of the function,
so O(mn)

Space complexity
O(nm) for dictionary
"""


s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s, t))
