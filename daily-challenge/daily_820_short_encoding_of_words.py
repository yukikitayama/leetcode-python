from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            # Try all the suffixes in a word
            # and remove the word which is a suffix of another word
            for k in range(1, len(word)):
                good.discard(word[k:])

        # +1 because we need to add # after a word
        return sum(len(word) + 1 for word in good)


if __name__ == '__main__':
    words = ["time", "me", "bell"]
    print(Solution().minimumLengthEncoding(words))
