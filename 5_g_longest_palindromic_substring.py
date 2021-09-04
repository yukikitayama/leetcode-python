class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 1:
            return ''

        start = 0
        end = 0

        for i in range(len(s)):
            # When center is a character, get length of a palindrome
            len1 = self.expand_around_center(s, i, i)
            # When center is between two characters, get length of a palindrome
            len2 = self.expand_around_center(s, i, i + 1)
            # We wanna have the longest
            length = max(len1, len2)

            # If we find a substring which is longer than what we recorded by end - start,
            # Update answer indices
            if length > end - start:
                # i is center-ish, so by minus and plus to get left end (start) and right end (end)
                start = i - (length - 1) // 2
                end = i + length // 2
                print(f'length: {length}, '
                      f's[start:end+1]: {s[start:end+1]}, '
                      f'start: {start}, '
                      f'end: {end}')

        return s[start:end+1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            # print(f'l: {l}, r: {r}, r - l - 1: {r - l - 1}')
        return r - l - 1


s = "babad"
# s = "cbbd"
print(Solution().longestPalindrome(s))
# print(Solution().expand_around_center(s, 2, 2))
# print(Solution().expand_around_center(s, 2, 3))
