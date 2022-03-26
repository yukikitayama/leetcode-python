"""
- make it string, and make it a list of characters
- for loop to check begin and end

- Above is not right, because we cannot convert integer to string
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Edge case: All negative are not palindrome for '-'
        if x < 0:
            return False

        # Edge case: If the rightmost last digit is 0,
        # only 0 itself is valid
        if x % 10 == 0 and x != 0:
            return False

        reverted_half = 0

        # print(f'x: {x}, reverted_half: {reverted_half}')

        while x > reverted_half:

            reverted_half = reverted_half * 10 + x % 10
            x //= 10

            # print(f'x: {x}, reverted_half: {reverted_half}')

        # reverted_half // 10 because the rightmost last digit of reverted_half
        # is the middle character if x was odd
        # e.g. 12321, 3 is obtained by reverted_half // 10
        # But from comparison view, we can ignore it
        return x == reverted_half or x == reverted_half // 10


if __name__ == '__main__':
    x = 1221
    x = 12321
    x = 123
    x = -1221
    print(Solution().isPalindrome(x))
