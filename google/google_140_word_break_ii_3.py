"""
Bottom up dynamic programming
- dp[i] represents the solution with s[0:i]
"""


from typing import List
from collections import defaultdict, Counter
import pprint


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # print(set(Counter(s).keys()))
        # print(set(Counter(''.join(wordDict)).keys()))

        # s contains a character which does not belong to wordDict,
        # we cannot break word
        s_char_set = set(Counter(s).keys())
        word_dict_char_set = set(Counter(''.join(wordDict)).keys())
        if s_char_set > word_dict_char_set:
            return []

        wordSet = set(wordDict)

        dp = [[]] * (len(s) + 1)

        # Base case
        dp[0] = ['']

        # print(f'dp: {dp}')

        for endIndex in range(1, len(s) + 1):
            sublist = []
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:

                        # print(f'  subsentence: {subsentence}, word: {word}')

                        sublist.append((subsentence + ' ' + word).strip())
            dp[endIndex] = sublist

        return dp[len(s)]


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s, wordDict))
