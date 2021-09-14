from typing import List
from collections import defaultdict
import pprint


class Master:
    def guess(self, word: str) -> int:
        return 0


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        # Count word in wordlist by combination of index and character
        place_counts = defaultdict(int)
        for word in wordlist:
            for i, char in enumerate(word):
                place_counts[str(i) + char] += 1
        # print(f'place_counts:')
        # pprint.pprint(place_counts)

        # Score is the sum of the frequency of the combination of index and character in wordlist
        # But what do high score or low score mean?
        # I guess if a word is more different from other words, this score gets lower
        def word_uniqueness(word):
            score = 0
            for i, char in enumerate(word):
                score += place_counts[str(i) + char]
                # print(f'str(i): {str(i)}, char: {char}, place_counts[str(i) + char]: {place_counts[str(i) + char]}')
            return score

        # print(f'word_uniqueness(wordlist[0]): {word_uniqueness(wordlist[0])}')
        # for i, word in enumerate(wordlist):
        #     print(f'word: {word}, word_uniqueness(wordlist[i]): {word_uniqueness(wordlist[i])}')

        # wordlist is sorted from very unique word (meaing doesn't share so many characters with other word)
        # to least unique (meaning share many characters with other word)
        wordlist.sort(key=word_uniqueness)
        # print(f'wordlist after sorting by word_uniqueness:\n{wordlist}')

        # ?
        # word is a word from wordlist
        # matches is integer representing the number of matches in terms of index and character to secret word
        # if matches is 1,
        # This function tries to find the next candidates. It returns True if it's worth it to be a candidate,
        # otherwise False
        # This function will be called after each guessing. mater.guess API will give us the integer matches,
        # and this functions tries to find different words from the used guess_word,
        # but it shares the same integer matches, so it's a candidate
        def word_is_possible(guess_word: str, word: str, matches: int):
            # guess_word is already used for guessing, so we don't wanna use it again,
            # so return False as it's not a candidate
            if guess_word == word:
                return False

            match_count = 0

            # Calculate the integer matches for the new given word in wordlist
            for a, b in zip(guess_word, word):
                if a == b:
                    match_count += 1
            # if match_count is equal to matches, it's a candidate because
            # the next new word shares the same integer matches in terms of index and character
            return match_count == matches

        # Just an idea to start from common word
        end = -1

        for _ in range(10):
            # Get guess word which is the least unique
            guess_word = wordlist[end]
            # matches contains integer representing the number of matches in terms of index and character
            matches = master.guess(guess_word)

            # Guessed the secret so break out of this for loop
            if matches == 6:
                # Break because the problem wants to know the number of master API calls
                break

            # I think we only visit here only until we get integer matches more than 0
            # all the calls after getting more than 0, we always go to the last else statement
            elif matches == 0:
                # Update wordlist from the result of master API calls by
                # removing words with the guess word which is not useful for secret
                # because it doesn't share anything with secret
                # if not any(xxx) gives us the word which does not share any characters at all with the useless word
                wordlist = [w for w in wordlist if not any(a == b for a, b in zip(guess_word, w))]

                # ?
                # Even if I comment out the below, it can still solve in LeetCode IDE
                if end == 0:
                    end = -1

            else:
                # matches could be from 1 to 5
                wordlist = [w for w in wordlist if word_is_possible(guess_word, w, matches)]

                # The above found candidates, and the below tries to use a guess_word,
                # which has sharing, but the most different (unique) word for guessing.
                if end == -1:
                    end = 0


wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
print(Solution().findSecretWord(wordlist, Master()))
