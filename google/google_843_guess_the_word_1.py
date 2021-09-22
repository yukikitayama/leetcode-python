from typing import List
from collections import defaultdict
import pprint


class Solution:
    def findSecretWord(self, wordlist: List[str], master) -> None:
        place_counts = defaultdict(int)
        for word in wordlist:
            for i, char in enumerate(word):
                place_counts[str(i) + char] += 1

        # pprint.pprint(place_counts)

        def common_score(word):
            score = 0
            for i, char in enumerate(word):
                score += place_counts[str(i) + char]
            return score

        # Sort word list from unique to common
        wordlist.sort(key=common_score)

        def is_candidate(guess_word, word, matches):
            if guess_word == word:
                return False

            match_count = 0
            for a, b in zip(guess_word, word):
                if a == b:
                    match_count += 1

            return match_count == matches


        # Start from very common to reduce the number of candidates
        word_selector = -1

        for _ in range(10):

            guess_word = wordlist[word_selector]

            matches = master.guess(guess_word)

            if matches == 6:
                break

            elif matches == 0:

                # Update word list
                wordlist = [word for word in wordlist if not any(a == b for a, b in zip(guess_word, word))]

            else:
                # Update word list
                wordlist = [word for word in wordlist if is_candidate(guess_word, word, matches)]

                word_selector = 0

"""
Algorithm
- Because we wanna know matches of a character and its index, we count what those 
  variety we have in wordlist
- Sort wordlist by uniqueness from unique to common
  - Make function to score uniqueness of each word in wordlist
  - For each character in a word, count up the value in dictionary of char-index to count
    - High count means index and character of a word is shared with many other words in wordlist
- Make a function to update wordlist
  - This will be called after we make a guess. 
    - We study something from the response of guess(), and update
  - 

- Make a for loop with 10 iterations
  - Pick a word
  - Guess by master.guess()
  - If the response from guess() is 6, break
  - If the response is 0, 
    - Remove the other words which have the same condition as the current word
  - If the response is > 0 and < 6
    - Update wordlist

"""

secret = "acckzz"
wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
print(Solution().findSecretWord(wordlist, None))
