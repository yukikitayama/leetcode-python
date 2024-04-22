"""
Hashmap
"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_hashmap = dict()
        upper_hashmap = dict()

        for i in range(len(word)):

            if word[i].islower():
                lower_hashmap[word[i]] = i

            elif word[i].isupper() and word[i].lower() not in upper_hashmap:
                upper_hashmap[word[i].lower()] = i

        candidates = set(lower_hashmap.keys()).intersection(set(upper_hashmap.keys()))
        ans = 0

        # print(lower_hashmap)
        # print(upper_hashmap)

        for candidate in candidates:

            if lower_hashmap[candidate] < upper_hashmap[candidate]:
                ans += 1

        return ans
