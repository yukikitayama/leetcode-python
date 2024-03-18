import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)

        odds = 0

        for k, v in counter.items():
            if v % 2 == 1:
                odds += 1

            if odds == 2:
                return False

        return True