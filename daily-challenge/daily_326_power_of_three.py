
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # Because 0 % something is 0
        if n == 0:
            return False

        while n % 3 == 0:
            n /= 3

        # If n is negative, it won't be 1 and power of three definition is
        # n == 3^x, so it won't be negative
        return n == 1


if __name__ == '__main__':
    n = 27
    n = 0
    n = 9
    n = -9
    print(Solution().isPowerOfThree(n))
