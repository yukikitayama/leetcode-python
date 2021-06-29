from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        heads = [[] for _ in range(26)]

        for word in words:
            it = iter(word)
            # a: 97, b: 98, .... z: 122
            # heads[0]: 'a' list, heads[1]: 'b' list
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in s:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                # None is returned when it is used up
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans



s = "abcde"
words = ["a","bb","acd","ace"]
Solution().numMatchingSubseq(s, words)