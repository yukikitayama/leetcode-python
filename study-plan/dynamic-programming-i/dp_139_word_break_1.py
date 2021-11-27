from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = [False] * (len(s) + 1)

        # Base case
        dp[0] = True

        for i in range(1, len(s) + 1):

            # print(f'i: {i}')

            for j in range(i):

                # print(f'j: {j}')

                # print(f'dp[j]: {dp[j]}, s[j:i]: {s[j:i]}')

                if dp[j] and s[j:i] in word_set:
                    dp[i] = True

                    # print(f'dp[i]: {dp[i]}, break')

                    break

        return dp[len(s)]


"""
Bottom up dynamic programming
Time: O(n^2), space: O(n)
"""


s = 'abc'
wordDict = ['a', 'bc']
print(Solution().wordBreak(s, wordDict))
