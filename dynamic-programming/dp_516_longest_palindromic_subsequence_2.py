"""
Algorithm: Top down dynamic programming with recursion with memoization
- We need to find palindrome so need to have two pointers from both side
  - As long as both side has the same characters it's guaranteed to be palindrome
- Then use recursive call to find the longest length
- dp(l, r) is the length of the longest palindromic subsequence of s[l:r]


"""


from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(l, r):

            # print(f'left: {l}, s[l]: {s[l]}, right: {r}, s[r]: {s[r]}')

            # Left index is bigger than right index meaning it crossed so it's an empty string
            if l > r:

                # print(f'  dp({l}, {r}): {0}')

                return 0

            # If current left and right indices are the same,
            # we only have a single character, and it must be the same character, so return 1
            if l == r:

                # print(f'  dp({l}, {r}): {1}')

                return 1

            # If current characters at left and right are the same,
            # We can add 2 length to answer and need to move both left and right indices,
            # to recursively find more characters from outside to inside to be a palindromic subsequence
            if s[l] == s[r]:

                # print(f'  dp({l}, {r}): dp({l + 1}, {r - 1}) + 2')

                return dp(l+1, r-1) + 2

            # If the current characters are not the same,
            # move either left or right index inside to find palindrome
            # Since they are not the same, nothing to be added.

            # print(f'  dp({l}, {r}): max(dp({l}, {r - 1}), dp({l +1}, {r})')

            return max(dp(l, r-1), dp(l+1, r))

        return dp(0, n - 1)


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))

