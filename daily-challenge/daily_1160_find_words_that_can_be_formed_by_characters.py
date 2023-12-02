from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars = collections.Counter(chars)

        ans = 0

        for word in words:
            count_word = collections.Counter(word)

            if count_word <= count_chars:

                ans += len(word)

        return ans


if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    print(Solution().countCharacters(words, chars))
