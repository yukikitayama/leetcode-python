from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter_chars = collections.Counter(chars)

        ans = 0

        for word in words:

            counter_word = collections.Counter(word)

            for char in counter_word:

                if counter_word[char] > counter_chars[char]:
                    break

            else:
                ans += len(word)

        return ans


if __name__ == '__main__':
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    # 6
    print(Solution().countCharacters(words, chars))
