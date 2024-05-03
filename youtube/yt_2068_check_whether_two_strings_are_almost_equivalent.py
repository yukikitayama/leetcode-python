import collections


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = collections.Counter(word1)
        counter2 = collections.Counter(word2)
        diff_max = float("-inf")

        for k, v in counter1.items():
            diff_max = max(diff_max, abs(v - counter2[k]))

        for k, v in counter2.items():
            diff_max = max(diff_max, abs(v - counter1[k]))

        return diff_max <= 3