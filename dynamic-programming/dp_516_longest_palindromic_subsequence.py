class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # print(f's: {s}')

        n = len(s)

        # Base case
        dp = [1] * n

        # j is the ending index in s
        for j in range(1, len(s)):

            # Save temporarily because inner for loop updates dp array in place
            pre = dp[j]

            # print(f'j: {j}, pre: {pre}')

            # i is the starting ending in s, but iterating from inside to outside
            for i in reversed(range(0, j)):

                # print(f'  i: {i}, s[i]: {s[i]}, s[j]: {s[j]}')

                tmp = dp[i]

                # i won't be overlapped with j. the below if finds two characters to form a palindromic subsequence
                if s[i] == s[j]:

                    # print(f'    in if: i + 1: {i + 1}, j - 1: {j - 1}')

                    # If i + 1 <= j - 1, then there's at least one character between s[i] and s[j]
                    # so you can append pre to the the longest subsequence so far
                    # otherwise there's no space for a character, so else 2 for the currently find s[i] and s[j]
                    # e.g. i: 0, j: 2, i + 1: 1, j - 1: 1, so one character between i: 0 and j: 2
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:

                    # print(f'    In else: dp[i + 1]: {dp[i + 1]}, dp[i]: {dp[i]}')

                    # Bottom up from the j, because first iteration i + 1 = j
                    dp[i] = max(dp[i + 1], dp[i])

                pre = tmp

                # print(f'      dp: {dp}')
                # print()

        return dp[0]




"""
Eventually, dp[i] contains the longest palindromic subsequence from i to the end of the array.
But during iteration, dp[i] is the currently found longest palindromic subsequence from i to the current j.
So in the end return dp[0]
"""

s = 'bbbab'
s = 'abcab'
print(Solution().longestPalindromeSubseq(s))
