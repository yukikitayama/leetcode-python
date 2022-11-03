from typing import List
import collections


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        counter = collections.Counter(words)

        # In for loop, increment ans by the number of words,
        # But at the end double it, because the problem asks us the length of the concatenated words,
        # not the number of words
        ans = 0

        central = False

        for word, count in counter.items():

            # If a word itself is a palindrome
            if word[0] == word[1]:

                # If count is even, no need to be used as central
                if count % 2 == 0:
                    ans += count

                else:
                    central = True
                    ans += (count - 1)

            # If a word is not a palindrome
            # e.g. if ab, but not care ba
            elif word[0] < word[1]:

                min_num = min(count, counter[word[1] + word[0]])
                ans += 2 * min_num

        if central:
            ans += 1

        ans *= 2

        return ans


if __name__ == '__main__':
    words = ["lc", "cl", "gg"]
    print(Solution().longestPalindrome(words))
