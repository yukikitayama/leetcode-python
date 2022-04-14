"""
- Find longest

- Find reverse in the list if the word has 2 different letters
- If the word has 2 same letters, find another to be not in middle, or middle
"""


from typing import List
import collections


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_to_count = collections.defaultdict(int)

        # Number of unpaired words with both letters same in a word
        unpaired_same = 0
        ans = 0

        for word in words:

            # If both letters are same
            if word[0] == word[1]:
                # If we have seen this word
                if word_to_count[word] > 0:
                    # We can pair them
                    unpaired_same -= 1
                    # Because we made a pair, reduced the number of record
                    word_to_count[word] -= 1

                    # The pair makes a palindrome, e.g. 'aaaa'
                    ans += 4

                # If we haven't seen this word
                else:
                    # Record it and flag unpaired
                    word_to_count[word] += 1
                    unpaired_same += 1

            # If a word has different letters
            else:

                # If we have found the reverse of the current word
                if word_to_count[word[::-1]] > 0:
                    # Make a palindrome
                    ans += 4
                    # Decrement because we used it to make a pair
                    word_to_count[word[::-1]] -= 1

                # If we haven't see the reverse
                else:
                    # Record it
                    word_to_count[word] += 1

        # If unpaired same letters word is left, insert it in the middle
        # e.g. palindrome is 'aaaa', we have unpaired 'bb',
        # longer palindrome is 'aabbaa'
        if unpaired_same > 0:
            ans += 2

        return ans


if __name__ == '__main__':
    words = ["lc", "cl", "gg"]
    words = ['aa', 'aa', 'bb']
    words = ['aa', 'aa', 'aa', 'aa']
    words = ['aa', 'aa', 'aa', 'bb']
    print(Solution().longestPalindrome(words))
