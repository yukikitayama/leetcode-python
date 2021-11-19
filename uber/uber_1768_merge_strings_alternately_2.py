import itertools


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # char1 + char2 because character from word1 is first
        # '' + char if either finishes earlier
        ans = [char1 + char2 for char1, char2 in itertools.zip_longest(word1, word2, fillvalue='')]

        # print(ans)

        return ''.join(ans)


"""
Complexity
- Time is O(max(n + m)) = O(m + n)
- Space is O(n + m)
"""


word1 = "abc"
word2 = "pqr"
# "apbqcr"
word1 = "ab"
word2 = "pqrs"
# "apbqrs"
print(Solution().mergeAlternately(word1, word2))


