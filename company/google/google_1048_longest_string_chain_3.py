"""
Bottom up dp

"""


from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_to_length = {}
        words.sort(key=lambda x: len(x))

        ans = 1

        for word in words:
            current_length = 1

            for i in range(len(word)):
                word_one_deleted = word[:i] + word[i + 1:]

                predecessor_length = word_to_length.get(word_one_deleted, 0)

                current_length = max(current_length, 1 + predecessor_length)

            word_to_length[word] = current_length

            ans = max(ans, current_length)

        return ans



words = ["a","b","ba","bca","bda","bdca"]
print(Solution().longestStrChain(words))
