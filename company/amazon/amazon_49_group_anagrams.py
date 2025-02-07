from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_words = collections.defaultdict(list)

        for str_ in strs:

            counter = [0] * 26
            for char in str_:
                counter[ord(char) - ord("a")] += 1
            key_to_words[tuple(counter)].append(str_)

        return list(key_to_words.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        key_to_words = collections.defaultdict(list)

        for str_ in strs:

            counter = [0] * 26
            for char in str_:
                counter[ord(char) - ord("a")] += 1
            key = []
            for i in range(len(counter)):
                if counter[i] != 0:
                    key.append(i)
                    key.append(counter[i])

            key_to_words[tuple(key)].append(str_)

        ans = []
        for k, v in key_to_words.items():
            ans.append(v)
        return ans
