import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = collections.Counter(word1)
        counter2 = collections.Counter(word2)

        counter_val1 = collections.Counter(counter1.values())
        counter_val2 = collections.Counter(counter2.values())

        return counter1.keys() == counter2.keys() and counter_val1 == counter_val2