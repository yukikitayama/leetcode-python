"""
- Length of 2 words need to be same
- Counter
"""


import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counter_1 = collections.Counter(word1)
        counter_2 = collections.Counter(word2)

        # print(f'counter_1: {counter_1}, counter_2: {counter_2}')

        if counter_1.keys() != counter_2.keys():
            return False

        return sorted(list(counter_1.values())) == sorted(list(counter_2.values()))


if __name__ == '__main__':
    word1 = 'abc'
    word2 = 'bca'
    word1 = "a"
    word2 = "aa"
    word1 = "cabbba"
    word2 = "abbccc"
    print(Solution().closeStrings(word1, word2))
