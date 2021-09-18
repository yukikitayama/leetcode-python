from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        heads = [[] for _ in range(26)]

        for word in words:
            it = iter(word)
            # the first character of a word is index
            # The element at the index in the array is the iterator starting from the second character
            first_character = next(it)
            index = ord(first_character) - ord('a')
            heads[index].append(it)
            # print(f'First character: {first_character}, '
            #       f'the index: {index}, '
            #       f'value appended to the array: {list(it)}')

        # for elements in head:
        #     for element in elements:
        #         print(list(element))

        for letter in s:
            # print(f'letter: {letter}')

            letter_index = ord(letter) - ord('a')
            # old_bucket is list of iterators
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                # it is a iterator
                it = old_bucket.pop()
                # Second argument is default
                nxt = next(it, None)
                # print(f'nxt: {nxt}')

                # If nxt is not None, a word in words is not finished yet, so save the next iterator to heads
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)

                # if nxt is None, it means that a word in words finished
                # So a word can be a subsequence of s, increment answer
                else:
                    ans += 1

        return ans


"""
Time complexity
Let m be the length of s, and n be the length of words
O(m + n*each word length)

Space complexity
O(n) for heads
"""


s = 'abcde'
words = ["a","bb","acd","ace"]
print(Solution().numMatchingSubseq(s, words))
