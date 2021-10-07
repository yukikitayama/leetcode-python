"""
max so far
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Edge case just in case, but constraints says 1 <= s.length <= 1000
        if s is None or len(s) < 1:
            return ''

        start = 0
        end = 0

        for i in range(len(s)):

            # print(f'i: {i}')

            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)

            # print(f'len1: {len1}, len2: {len2}')

            length = max(len1, len2)

            # Update longest
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
                # print(f'length: {length}, '
                #       f's[start:end+1]: {s[start:end+1]}, '
                #       f'start: {start}, '
                #       f'end: {end}')

        return s[start:end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        """
        It starts at the center and two pointers go toward left edge
        and right edge. It returns the longest length of a palindrome found
        """

        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        # print(f'l: {l}, r: {r}, r - l - 1: {r - l - 1}')
        # -1 because always l or r is out of index when while is false
        return r - l - 1


s = 'aba'
s = 'a'
s = 'aa'
print(Solution().longestPalindrome(s))




