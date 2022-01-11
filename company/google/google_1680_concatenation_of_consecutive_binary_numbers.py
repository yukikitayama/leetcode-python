import math


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        length = 0
        result = 0

        for i in range(1, n + 1):

            if i & (i - 1) == 0:
                length += 1

            # Left-shift and fill the new right space with i
            result = ((result << length) | i) % (10**9 + 7)

        return result


class Solution2:
    def concatenatedBinary(self, n: int) -> int:
        length = 0
        result = 0

        for i in range(1, n + 1):
            if math.log(i, 2).is_integer():
                length += 1

            # 2 ** length does left-shift
            # and + i fills a number to the right new space
            result = ((2 ** length) * result + i) % (10**9 + 7)

        return result


class Solution1:
    def concatenatedBinary(self, n: int) -> int:
        binary = ''
        for i in range(1, n + 1):
            binary += bin(i)[2:]

        # print(f'Binary: {binary}')

        return int(binary, 2) % (10**9 + 7)


if __name__ == '__main__':
    n = 3
    n = 12  # 505379714
    print(Solution().concatenatedBinary(n))
