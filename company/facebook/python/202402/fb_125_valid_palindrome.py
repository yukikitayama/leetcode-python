"""
preprocess the given string

How to identify all non-alphanumetic characters

two pointer
  from leftmost and from rightmost
  when two characters are not the same
    return False
  iterate towards center
"""


class Solution:
    # def isPalindrome(self, s: str) -> bool:

    #     s = s.replace(" ", "")

    #     if not s:
    #         return True

    #     alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    #     s = [ch.lower() for ch in s if ch in alphanumeric]

    #     # print(s)

    #     left = 0
    #     right = len(s) - 1

    #     while left <= right:

    #         if s[left] != s[right]:
    #             return False

    #         left += 1
    #         right -= 1

    #     return True

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left <= right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
