"""
Top down recursion with memoization

"""


from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Key: word, value: max length
        memo = {}
        wordsPresent = set(words)
        ans = 0
        for word in words:
            ans = max(ans, self.dfs(wordsPresent, memo, word))

        return ans

    def dfs(self, words: set, memo: dict, currentWord: str) -> int:
        if currentWord in memo:
            return memo[currentWord]

        maxLength = 1

        for i in range(len(currentWord)):
            newWord = currentWord[:i] + currentWord[i + 1:]

            if newWord in words:
                currentLength = 1 + self.dfs(words, memo, newWord)
                maxLength = max(maxLength, currentLength)

        memo[currentWord] = maxLength

        return maxLength


words = ["a","b","ba","bca","bda","bdca"]
print(Solution().longestStrChain(words))

