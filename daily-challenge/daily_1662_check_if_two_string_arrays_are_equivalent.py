from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return True if ''.join(word1) == ''.join(word2) else False


if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(Solution().arrayStringsAreEqual(word1, word2))
