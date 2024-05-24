"""
Hashmap
  k: letter in letters
  v: count
Compute score of each word

Ans
  midified version of backtracking
"""

from typing import List
import collections


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        word_to_score_counter = collections.defaultdict(list)
        for word in words:
            if word in word_to_score_counter:
                continue

            s = 0
            for ch in word:
                i = ord(ch) - ord("a")
                s += score[i]

            word_to_score_counter[word].append(s)
            word_to_score_counter[word].append(collections.Counter(word))

        letter_counter = collections.Counter(letters)

        ans = float("-inf")

        def backtracking(index, curr_sum, curr_counter):
            nonlocal ans

            if index == len(words):
                ans = max(curr_sum, ans)
                return

            word = words[index]
            word_score, word_counter = word_to_score_counter[word]

            valid = True
            for k, v in word_counter.items():
                if k not in curr_counter:
                    valid = False
                elif curr_counter[k] < v:
                    valid = False

            # Include
            if valid:
                curr_counter -= word_counter

                backtracking(index + 1, curr_sum + word_score, curr_counter)

                # Backtrack
                curr_counter += word_counter

            # Exclude
            backtracking(index + 1, curr_sum, curr_counter)

        backtracking(0, 0, letter_counter)

        return 0 if ans == float("-inf") else ans