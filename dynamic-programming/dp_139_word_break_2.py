"""
Brute force
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def wordBreakRecur(s, word_dict, start):

            print(f'In wordBreakRecur: start: {start}')

            if start == len(s):
                print(f'    start == len(s)')
                return True

            # Python ending slicer is exclusive, so to include the last character in s
            # we need to use index of len(s), so len(s) + 1, because ending range is also exclusive
            for end in range(start + 1, len(s) + 1):

                print(f'  s[start:end]: {s[start:end]}, start: {start}, end: {end}')

                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True

            return False

        return wordBreakRecur(s, set(wordDict), 0)


s = "leetcode"
wordDict = ["leet","code"]
s = "applepenapple"
wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(Solution().wordBreak(s, wordDict))

