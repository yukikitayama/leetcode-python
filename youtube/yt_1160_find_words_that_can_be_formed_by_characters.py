from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter_chars = collections.Counter(chars)

        ans = 0

        for i in range(len(words)):

            counter_word = collections.Counter(words[i])
            valid = True

            for k, v in counter_word.items():

                if k not in counter_chars:
                    valid = False

                elif v > counter_chars[k]:
                    valid = False

            if valid:
                ans += len(words[i])

        return ans
