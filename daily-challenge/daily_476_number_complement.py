import math


class Solution:
    def findComplement(self, num: int) -> int:
        n = math.floor(math.log2(num)) + 1
        bitmask = (1 << n) - 1

        print(f'n: {n}')

        return bitmask ^ num


class Solution1:
    def findComplement(self, num: int) -> int:
        todo = num
        bit = 1
        while todo:
            # XOR from right to left
            num = num ^ bit
            bit = bit << 1

            # to_do counts the number of digit in num
            todo = todo >> 1

        return num


if __name__ == '__main__':
    num = 5
    print(Solution().findComplement(num))