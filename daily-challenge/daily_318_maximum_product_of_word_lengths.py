from typing import List
import collections


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask_to_max_len = collections.defaultdict(int)
        bit_number = lambda ch: ord(ch) - ord('a')

        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << bit_number(ch)
            bitmask_to_max_len[bitmask] = max(bitmask_to_max_len[bitmask], len(word))

        ans = 0
        for i in bitmask_to_max_len:
            for j in bitmask_to_max_len:
                # If no share common letters
                if i & j == 0:
                    ans = max(ans, bitmask_to_max_len[i] * bitmask_to_max_len[j])
        return ans


class Solution1:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        bit_number = lambda ch: ord(ch) - ord('a')

        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                bitmask |= 1 << bit_number(ch)
            masks[i] = bitmask
            lens[i] = len(words[i])

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, lens[i] * lens[j])
        return ans


if __name__ == '__main__':
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(Solution().maxProduct(words))
