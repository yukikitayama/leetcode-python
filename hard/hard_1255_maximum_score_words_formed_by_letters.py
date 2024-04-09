"""
Convert each word to total score
Convert each word to hashmap
Convert letters to hashmap

Backtracking
word length max 14
  2**14 = 16,384
"""

from typing import List
import collections


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_counter = collections.Counter(letters)
        word_to_score_counter = collections.defaultdict(list)
        for word in words:
            # words could contain duplicated word
            if word in word_to_score_counter:
                continue

            s = 0
            for ch in word:
                i = ord(ch) - ord("a")
                s += score[i]
            word_to_score_counter[word].append(s)
            word_to_score_counter[word].append(collections.Counter(word))

        # print(letter_counter)
        # print(word_to_score_counter)
        # print()

        ans = float("-inf")

        def backtracking(curr_sum, curr_idx, counter):
            nonlocal ans

            if curr_idx == len(words):
                ans = max(ans, curr_sum)
                return

            for i in range(curr_idx, len(words)):
                word = words[i]
                score, word_counter = word_to_score_counter[word]

                valid = True
                for k, v in word_counter.items():
                    if k not in counter:
                        valid = False
                    elif counter[k] - v < 0:
                        valid = False

                # If valid, we gain the score, update counter, and go to the next word
                if valid:
                    counter -= word_counter

                    backtracking(curr_sum + score, i + 1, counter)

                    # Backtrack
                    counter += word_counter

                # If not valid, we still go to the next word, but no score gain, and no counter update
                else:
                    backtracking(curr_sum, i + 1, counter)

        backtracking(0, 0, letter_counter)

        return 0 if ans == float("-inf") else ans