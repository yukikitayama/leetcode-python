from typing import List
from collections import defaultdict


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        index_char_to_count = defaultdict(int)
        for word in wordlist:
            for i, char in enumerate(word):
                index_char_to_count[str(i) + char] += 1

        def common_score(word):
            score = 0
            for i, char in enumerate(word):
                score += index_char_to_count[str(i) + char]
            return score

        wordlist.sort(key=common_score)

        def check_match(word_to_guess: str, curr_word: str, match: int) -> bool:
            if word_to_guess == curr_word:
                return False

            counter = 0
            for char1, char2 in zip(word_to_guess, curr_word):
                if char1 == char2:
                    counter += 1

            return counter == match

        word_selector = -1

        for _ in range(10):

            word_to_guess = wordlist[word_selector]

            match = master.guess(word_to_guess)

            if match == 6:
                break

            else:
                wordlist = [word for word in wordlist if check_match(word_to_guess, word, match)]
