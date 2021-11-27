from collections import defaultdict
from typing import List
import pprint


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        waiting = defaultdict(list)

        for w in words:

            # print(f'w: {w}')

            waiting[w[0]].append(iter(w[1:]))

        # print('waiting')
        # pprint.pprint(waiting)
        # print()

        for c in s:

            # print(f'  c: {c}')

            # Python dictionary pop() removes and returns an element
            # From the dictionary with the key. If not exist, default will
            # be popped if specified
            for iterator in waiting.pop(c, ()):

                # next() returns the second argument if the iterator is exhausted
                # None key dictionary holds the list of subsequeces found in s as value
                # If next(iterator, None) is None all the characters in word are found in s
                # When exhausted waiting dictionary contains a value of stopIteration iterator object
                # We don't care about the content of iterator, we just wanna know how many such
                # iterators we have in the end
                waiting[next(iterator, None)].append(iterator)

        # print('waiting:')
        # pprint.pprint(waiting)

        return len(waiting[None])


s = "abcde"
words = ["a","bb","acd","ace"]
print(Solution().numMatchingSubseq(s, words))
