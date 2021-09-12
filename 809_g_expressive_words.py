from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s_letters, s_counts = self.compress(s)
        res = 0
        for word in words:
            if self.is_stretchy(word, s_letters, s_counts):
                res += 1

        return res

    def compress(self, word):
        letters = []
        counts = []

        for l in word:

            # When it's the first time or not same as previous letter in letters
            # This only checks one previous letter, so we could have
            # letters: ['a', 'b', 'a'], multiples of the same letter like 'a'
            if not letters or l != letters[-1]:
                letters.append(l)
                counts.append(1)
            else:
                counts[-1] += 1

        return letters, counts

    def is_stretchy(self, word, s_letters, s_counts):
        w_letters, w_counts = self.compress(word)

        # w_letters == s_letters is True if the lists of character sequences are the same
        # if the distinct letters sequence are not the same,
        # it's impossible for query word to be s by extension operation
        if w_letters != s_letters:
            return False

        for i in range(len(s_counts)):
            # If s count is less than 3, query word can't do extension operation,
            # so to be the same, query word already needs to have the same number of letters
            if s_counts[i] < 3 and s_counts[i] != w_counts[i]:
                return False

            # To do extension, query word letter counts need to be less than or equal to s counts
            if s_counts[i] >= 3 and s_counts[i] < w_counts[i]:
                return False

        return True


"""
Time complexity
Let n be the length of words, m be the length of s, 
O(m) to compress s, O(m) to compress each word in words
O(n) to iterate each word in words
O(m) to iterate each letter in is_stretchy
so, O(m) + O(n * m) + O(m) = O(2m + nm) = O(nm)

Space complexity
O(2m) to store s letters and counts array, same for word
so O(n + m)
"""


s = "heeellooo"
words = ["hello", "hi", "helo"]
s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]
print(Solution().expressiveWords(s, words))
