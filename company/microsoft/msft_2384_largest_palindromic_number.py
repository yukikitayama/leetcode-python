"""
Largest palindromic number
  longest length
  largest digits at left

Counter
  all even
  all even except one odd
"""

import collections


class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = collections.Counter(num)

        # print(counter)

        side = []

        # Create left side from the largest digit
        # Get only the ones which can make pairs for palindrome
        for digit in "9876543210":
            side.append(counter[digit] // 2 * digit)

        side = "".join(side)
        # Leading 0 are not allowed
        # lstrip("character") removes leading characters
        side = side.lstrip("0")

        # print(side)

        mid = ""
        for digit in counter:

            if counter[digit] % 2 != 0:
                mid = max(mid, digit)

        # print(mid)

        if side + mid + side[::-1]:
            return side + mid + side[::-1]
        # When given num is "000000", the above returns "" but we wanna return "0"
        else:
            return "0"