"""
check if the given s is palindrome

iterate s
  remove curent character and check palindrome
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(word, left, right):
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return palindrome(s, left + 1, right) or palindrome(s, left, right - 1)

            else:
                left += 1
                right -= 1

        return True