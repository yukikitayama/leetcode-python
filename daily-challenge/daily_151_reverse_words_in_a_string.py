"""
- ['a', 'b', 'c', ' ', 'd']
- end: 3, start: 0,
- reverse
- start: 4, end: 4

Algorithm
- trim the leading and trailing spaces and put string into list of characters
- reverse the list
- reverse each word
- join the list with a space into string

Complexity
- Time is O(n) to trim extra spaces, to reverse it, and reverse each word
- Space is O(n) to make a list of characters from the given s
"""


from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:

        l = self.trim_spaces(s)

        # print(f'l: {l}')

        self.reverse(l, 0, len(l) - 1)

        # print(f'l: {l}')

        self.reverse_each_word(l)

        # print(f'l: {l}')

        # '' because the list of characters already contains spaces between words
        return ''.join(l)

    def trim_spaces(self, s: str) -> List[str]:
        left = 0
        right = len(s) - 1

        # When breaking out of the while loop, left is the correct start
        while left < right and s[left] == ' ':
            left += 1

        # The above is the same for right
        while left < right and s[right] == ' ':
            right -= 1

        l = []
        # <= because right is the last index of s
        # and left is the index to append character to the list
        # so left at the end needs to be right index to include the last character
        while left <= right:
            if s[left] != ' ':
                l.append(s[left])
            # Skip the consecutive 2nd space
            elif s[left] == ' ' and l[-1] != ' ':
                l.append(s[left])
            left += 1

        return l

    def reverse(self, l: List[str], left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l: List[str]) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # When breaking out of the while loop, end is space
            while end < n and l[end] != ' ':
                end += 1

            # -1 because end is currently space
            self.reverse(l, start, end - 1)

            # currently end is space, so the bellow allows start to be the starting of the next word
            start = end + 1
            # end = start
            end += 1


s = "the sky is blue"
print(Solution().reverseWords(s))


