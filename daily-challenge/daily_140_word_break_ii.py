from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)

        ans = []

        def backtracking(index, curr_comb):

            if index == len(s):
                ans.append(" ".join(curr_comb))
                return

            for end in range(index + 1, len(s) + 1):
                curr_word = s[index:end]

                if curr_word in word_set:
                    curr_comb.append(curr_word)
                    backtracking(end, curr_comb)

                    # Backtrack
                    curr_comb.pop()

        backtracking(0, [])

        return ans
