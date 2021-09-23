from typing import List


class Solution:
    def longestStrChain(self, words: List[int]) -> int:
        # Sort the list in an ascending order in terms of length of each word
        # because we wanna to answer from the base case, meaning shortest word,
        # and add up to longer words
        words.sort(key=lambda x: len(x))

        # print(words)

        # Dictionary with Key word, and Value: longest length
        word_to_length = {}

        # print(word_to_length)

        # We are guaranteed to have at least 1 because constraints says 1 <= words[i].length
        answer = 1

        for word in words:
            current_length = 1

            # print(f'word: {word}')

            for i in range(len(word)):

                word_one_deleted = word[:i] + word[i + 1:]

                # print(f'word_one_deleted: {word_one_deleted}')

                # If the key does not exist, give us default 0
                predecessor_length = word_to_length.get(word_one_deleted, 0)

                # + 1 because predecessor plus the current character
                current_length = max(current_length, predecessor_length + 1)

            word_to_length[word] = current_length

            answer = max(answer, current_length)

        return answer


# words = ["a","b","ba","bca","bda","bdca"]
# words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
words = ["abcd","dbqca"]
print(Solution().longestStrChain(words))
