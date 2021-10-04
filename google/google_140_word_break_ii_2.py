"""
Top down dynamic programming with memoization
"""


from typing import List
from collections import defaultdict
import pprint


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        # Key: valid postfix, Value: list of prefixes
        memo = defaultdict(list)

        def _wordBreak_topdown(s):
            if not s:
                return [[]]

            if s in memo:
                return memo[s]

            for endIndex in range(1, len(s) + 1):

                word = s[:endIndex]

                if word in wordSet:

                    for subsentence in _wordBreak_topdown(s[endIndex:]):

                        # print(f's: {s}, word: {word}, subsentence: {subsentence}')

                        memo[s].append([word] + subsentence)

            return memo[s]

        _wordBreak_topdown(s)

        # print(f'memo:')
        # pprint.pprint(memo)

        answers = []
        for words in memo[s]:
            answer = ' '.join(words)
            answers.append(answer)

        return answers




s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s, wordDict))
