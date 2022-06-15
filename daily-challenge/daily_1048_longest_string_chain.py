"""
- Start from longest and remove
"""


from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def dfs(words_present, memo, word):

            if word in memo:
                return memo[word]

            max_length = 1

            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]

                if new_word in words_present:
                    curr_length = 1 + dfs(words_present, memo, new_word)
                    max_length = max(max_length, curr_length)

            memo[word] = max_length
            return max_length

        memo = {}
        words_present = set(words)
        ans = 0

        for word in words:
            ans = max(ans, dfs(words_present, memo, word))

        return ans


if __name__ == '__main__':
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    # 4
    words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    # 5
    # words = ["abcd", "dbqca"]
    # 1
    print(Solution().longestStrChain(words))

    # word = 'abc'
    # i = 0
    # print(word[:i] + word[i+1:])
    # i = 1
    # print(word[:i] + word[i+1:])
