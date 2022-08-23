"""
- modulo 4?
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            print(f'n: {n}, n % 4: {n % 4}')
            n /= 4

        print(f'n: {n}, n % 4: {n % 4}')

        return n == 1


if __name__ == '__main__':
    n = 16
    # n = 5
    # n = 1
    # n = -2147483648
    print(Solution().isPowerOfFour(n))
