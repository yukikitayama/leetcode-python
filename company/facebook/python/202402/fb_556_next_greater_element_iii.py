"""
if digits are descending order
  return -1
Find the first 2 digits where they are ascending order and swap
  Scan from the right ensures that next greater number
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [ch for ch in str(n)]

        # From right, find the first 2 pair of ascending
        i = len(digits) - 2
        while 0 <= i and digits[i] >= digits[i + 1]:
            i -= 1

        # IF we couldn't find the pair, impossible to have the next greater
        if i < 0:
            return -1

        # In the right, find the next greater digit to teh found digit
        j = len(digits) - 1
        while i < j and digits[i] >= digits[j]:
            j -= 1

        # Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Reverse order at the right
        temp = digits[i + 1:]
        temp.reverse()
        digits[i + 1:] = temp

        ans = int("".join(digits))
        if ans >= 2 ** 31:
            return -1
        else:
            return ans
