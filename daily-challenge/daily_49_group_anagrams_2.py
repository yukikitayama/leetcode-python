from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_key_to_strs = collections.defaultdict(list)

        for s in strs:

            counter = [0] * 26

            for c in s:

                counter[ord(c) - ord("a")] += 1

            anagram_key_to_strs[tuple(counter)].append(s)

        return anagram_key_to_strs.values()





