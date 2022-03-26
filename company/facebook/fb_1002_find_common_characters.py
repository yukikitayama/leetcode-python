from typing import List
import collections


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = collections.Counter(words[0])

        for word in words[1:]:

            counter &= collections.Counter(word)

        return list(counter.elements())


class Solution1:
    def commonChars(self, words: List[str]) -> List[str]:
        for i, word in enumerate(words):

            if i == 0:
                counter = collections.Counter(word)

            else:
                counter = counter & collections.Counter(word)

        ans = []
        for k, v in counter.items():

            for _ in range(v):
                ans.append(k)

        return ans


if __name__ == '__main__':
    words = ["bella", "label", "roller"]
    print(Solution().commonChars(words))
