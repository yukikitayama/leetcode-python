"""
We have constrains, left and right represent integers in the range [1, 10**18]
For example, P = R**2 is a superpalindrome.
P < 10**18
R**2 < 10**18
R < (10**18)**(1/2)
R < 10**9
R is a palindrome, so for example k is a half of it, R = k|k', where | is concat and k' is a reverse of k.
So k < 10**5
"""


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # Initialize
        L = int(left)
        R = int(right)
        MAGIC = int(1e+5)
        ans = 0

        # Count how many superpalindromes with odd length number
        # k is a half of possible palindromes
        # For example, 1234321
        for k in range(1, MAGIC):
            first_half = str(k)
            # [-2::-1] gets the reverse of the original up to the second last
            # When k = '1234', k[-2::-1] = '321'
            second_half = str(k)[-2::-1]
            # Make a potential superpalindrome
            number = int(first_half + second_half) ** 2

            # Out of range
            if number > R:
                break

            # In range and it's superpalindrome
            if number >= L and self.is_palindrome(number):
                ans += 1

        # Count how many superpalindromes with even length number
        # For example, 12344321
        for k in range(1, MAGIC):
            first_half = str(k)
            second_half = str(k)[::-1]
            number = int(first_half + second_half) ** 2
            if number > R:
                break
            if number >= L and self.is_palindrome(number):
                ans += 1

        return ans

    def is_palindrome(self, x):
        return x == self.reverse(x)


    def reverse(self, x):
        # Initialize
        ans = 0

        while x > 0:

            # The below moves current ans to the left by one digit by (10 * ans),
            # gets first digit of x by (x % 10),
            # gets the remaining digits by (x // 10).
            # eventually the original rightmost first digit goes to the leftmost, so reversed
            # x = 1234 -> 4, 123 -> 43, 12 -> 432, 1 -> 4321
            # print(f'10 * ans: {10 * ans}, x % 10: {x % 10}, x / 10: {x // 10}')
            ans = 10 * ans + x % 10
            x //= 10

        return ans


def main():

    # Test
    left = '4'
    right = '1000'

    sol = Solution()
    x = 1234
    reversed_x = sol.reverse(x)
    print(f'x: {x}, reversed x: {reversed_x}')

    x = 121
    is_palindrome = sol.is_palindrome(x)
    print(f'Is palindrome?: {is_palindrome}')

    x = 1234
    # x = 12
    first = str(x)
    second = str(x)[-2::-1]
    print(f'First half: {first}, second half: {second}')

    ans = sol.superpalindromesInRange(left, right)
    print(f'Answer: {ans}')


if __name__ == '__main__':
    main()
