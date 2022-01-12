"""
- Find max absolute difference of indices of the same characters
- Ans is max_abs_diff - 1
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        indices = {}

        for i, c in enumerate(s):
            # When it encounters a new character for the first time,
            # the result is always -1,
            # e.g. i: 0, 0 - (0 + 1) = -1
            # e.g. i: 1, 1 - (1 + 1) = -1
            # Because the value of a key is fixed the first index for the character
            # getting value from the dictionary and taking the difference between i and the value
            # will produce bigger difference as iteration goes, so we can get the largest
            abs_diff = i - indices.setdefault(c, i + 1)
            ans = max(ans, abs_diff)

            # print(f'i: {i}, c: {c}, abs_diff: {abs_diff}, indices: {indices}')

        return ans


if __name__ == '__main__':
    s = 'aa'
    s = "abca"
    s = 'abcadefa'
    # Should be 6 by substring between the first a and the final a,
    # even if the substring contains another a.
    print(Solution().maxLengthBetweenEqualCharacters(s))
