"""
Whitespace
  The beginning whitespaces are simply removed
  The whitespace in the middle, discard current space to the rest of the stuff
Digits
  Remove leading zeros
  Otherwise read the digits until the first non-digits.
  If no digits, return 0
Sign
  leading at most sign will be used
  Afterward, sign in the middle let us stop building number
Anything else
  Treat it as the time to stop building number
32-bit integer range
"""

class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0

        # Check leading whitespaces
        while i < len(s) and s[i] == " ":
            i += 1

        # Check sign
        sign = 1
        if i < len(s) and s[i] == "+":
            sign = 1
            i += 1
        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        # Extract digit as long as current string is digit
        ans = 0
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        while i < len(s) and s[i].isdigit():

            digit = int(s[i])

            # Check overflow
            if ans > INT_MAX // 10:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            # INT_MAX % 10 = (pow(2, 31) - 1) % 10 = 2147483647 % 10 = 7
            elif ans == INT_MAX // 10:
                if digit == 8 or digit == 9:
                    if sign == 1:
                        return INT_MAX
                    elif sign == -1:
                        return INT_MIN

            ans = ans * 10 + digit
            i += 1

        return sign * ans


