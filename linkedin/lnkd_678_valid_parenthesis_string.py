"""
- brute force is to replace each * with '(', ' ', or ')',
  and check whether the replaced s is valid
- optimized solution O(n) as one pass to keep track of left parenthesis
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for char in s:

            # If we have currently open left brackets, we have more lower bound
            if char == '(':
                low += 1
            # If current character is ) or *, decrement lower bound
            else:
                low -= 1

            # If current character is ( or *, we can have more open left brackets
            if char != ')':
                high += 1
            # If current character is ), it decrement open left brackets
            else:
                high -= 1

            # If we have more right brackets than ( and *, we cannot close parenthesis
            if high < 0:
                break

            # Low is the number of possibilities that we have open left parenthesis
            # , so it must not be negative
            low = max(low, 0)

            # print(f'  low: {low}, high: {high}, char: {char}')

        # print(f'low: {low}, high: {high}')

        return low == 0


s = '()'
s = '(*)'
s = '())'
print(Solution().checkValidString(s))
