"""
Question
- What's the max length of wordlist?
- What's the length of each word in wordlist
- How can I stop this?
  - If it receives 6, does the test stop?
  - should I throw break?

Idea
- We need a function to filter a word with a specific match
  - If master().guess gives me 1, I wanna filter wordlist to be a wordlist which only contains the 1
  - We can reduce the size of wordlist, and increase the probability to get the secret, 6
- If the length of wordlist is less than or equal to 10, we can guess one by one
- To reduce the size, I wanna pick a word which is similar to other words
  - So if it isn't the secret, with one guess, we can exclude lots of words from wordlist for the next guess
    and probability is higher
  - So I need another function to quantify how similar a word is to wordlist

Algorithm
  - Filter function for each word
    - With a word, using master API, we receive integer 0 to 6
      - e.g. word: abcdef, secret: abczzz, response: 3, wordlist: [abcyyy, abcxxx, abcdef, xxxxxx]
        - We wanna remove abcdef (already used), and xxxxxx (does not share position and characters with abcdef)
        - But abcyyy, abcxxx is 3 same in position and characters as abcdef
"""


from typing import List
from collections import defaultdict


class Master:
    def guess(self, word: str) -> int:
        return 0


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        # Similar score quantify function
        # Position and character
        # Key: string of index and char, value: count
        index_char_to_count = defaultdict(int)
        for word in wordlist:
            for index, char in enumerate(word):
                index_char_to_count[str(index) + char] += 1

        def quantify_word(word):
            score = 0
            for index, char in enumerate(word):
                counter = index_char_to_count[str(index) + char]
                score += counter
            return score

        # Filter function
        def is_matched(curr_word, used_word: str, response: int) -> bool:
            if curr_word == used_word:
                return False

            counter = 0
            for char1, char2 in zip(curr_word, used_word):
                if char1 == char2:
                    counter += 1

            return counter == response

        # Start guessing
        # We wanna reduce the size, so start from the word which is similar to others
        wordlist.sort(key=quantify_word)
        # wordlist: unique -> similar

        for _ in range(10):

            word_to_guess = wordlist[-1]
            response = master.guess(word_to_guess)

            # If it got the secret, break
            if response == 6:
                break

            # If it didn't the secret, with the response of master API, filter wordlist, and reduce the size of wordlist
            else:
                wordlist = [word for word in wordlist if is_matched(word, word_to_guess, response)]

