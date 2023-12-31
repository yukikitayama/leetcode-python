"""
True if all the characters are divisible by the length of words list
"""

from typing import List
import collections


class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        counter = collections.Counter()

        for word in words:
            counter += collections.Counter(word)

        for k, v in counter.items():
            if v % len(words) != 0:
                return False
        return True


if __name__ == "__main__":
    words = ["abc", "aabc", "bc"]
    words = ["ab", "a"]
    print(Solution().makeEqual(words))
