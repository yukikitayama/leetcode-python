"""
hashmap, key character, value index in keyboard
curr = 0, iterate given word, compute each distance, sum, update curr
"""

import collections


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        char_to_idx = collections.defaultdict(int)

        for i in range(len(keyboard)):

            char_to_idx[keyboard[i]] = i

        ans = 0
        curr = 0

        for char in word:
            d = abs(char_to_idx[char] - curr)
            ans += d
            curr = char_to_idx[char]

        return ans


if __name__ == "__main__":
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
    print(Solution().calculateTime(keyboard, word))

