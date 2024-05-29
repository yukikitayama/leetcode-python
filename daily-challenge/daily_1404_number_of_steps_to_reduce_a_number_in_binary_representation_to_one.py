"""
Obs
  even: rightmost bit is 0
  odd: rightmost bit is 1
  8 / 2 = 4, 8: 1000, 4: 100
  divide by 2: right shift?
  5 + 1 = 6, 5: 101, 6: 110
  13 + 1 = 14, 13: 1101, 14: 1110
  1011: 11, 11 + 1 = 12, 12: 1100
  1111: 15, 15 + 1 = 16, 10000
  add 1: carry rightmost bit to left

eg
  1101: 13
  1110: 14 by adding 1
  0111: 7
  1000: 8 by adding 1
  0100: 4
  0010: 2
  0001: 1

Ans
  To add one to the string, we will start from the right end and keep adding 1 while the carry doesn't become zero. We can implement this by iterating from the right end and changing each 1 to 0 until we find the first 0. If we don't find any 0s we will have to append a 1 at the start of the string.
"""


class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):

            curr_digit = int(s[i]) + carry

            # Odd
            if curr_digit % 2 != 0:
                # +2 because, first make it even, then remove rightmost bit
                ans += 2
                carry = 1
            # Even
            else:
                ans += 1

        return ans + carry

    def numSteps2(self, s: str) -> int:

        def divide_by_two(s_list):
            s_list.pop()

        def add_one(s_list):
            i = len(s_list) - 1

            while i >= 0 and s_list[i] == "1":
                s_list[i] = "0"
                i -= 1

            # They were all "1"
            if i < 0:
                s_list.insert(0, "1")
            # First "0"
            else:
                s_list[i] = "1"

        ans = 0
        s_list = list(s)

        while len(s_list) > 1:
            n = len(s_list)

            # Even
            if s_list[n - 1] == "0":
                divide_by_two(s_list)
            # Odd
            else:
                add_one(s_list)

            ans += 1

        return ans

    def numSteps1(self, s: str) -> int:
        num = int(s, 2)
        print(num)
        ans = 0
        while num != 1:
            if num % 2 == 0:
                num /= 2
            elif num % 2 != 0:
                num += 1
            ans += 1
        return ans
