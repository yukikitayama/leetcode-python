"""
- dp[i] represents if it's possible to build the string s up to index i from wordDict.
- Return df[n - 1]

0 1 2 3

i: 2
word length: 2
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * len(s)

        # i is the current index in s, and the end index of a word
        for i in range(len(s)):

            for word in wordDict:

                # i >= len(word) - 1 is false means i is too early to contain whole characters in word
                # i == len(word) - 1 checks if word is the first word to form in s
                # dp[i - len(word)] checks if the previous word was fine
                # e.g. i: 2, word: 'bc', len(word): 2, i - len(word): 0,
                #      suppose the first was was 'a', so dp[0]: True
                # So this if condition means
                # if word is short enough to compare and (the first word or the previous word was fine)
                if i >= len(word) - 1 and (i == len(word) - 1 or dp[i - len(word)]):

                    # Check if the current word is fine
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        # Break the for loop of wordDict, not the most outer for loop
                        break

        return dp[-1]


