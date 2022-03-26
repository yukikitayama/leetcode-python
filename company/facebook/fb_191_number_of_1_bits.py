class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            # As long as n is not 0, we have 1
            ans += 1
            # n & (n - 1) turns off the least significant 1-bit
            # e.g. n: 4, bin(n): '100', n - 1: 3, bin(n - 1): '011',
            # '100' & '011' = '000'
            n &= (n - 1)
        return ans


class Solution1:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        mask = 1

        for _ in range(32):

            if n & mask != 0:
                ans += 1

            mask <<= 1

            # print(f'mask: {mask}, bin(mask): {bin(mask)}')

        return ans


if __name__ == '__main__':
    # print(int('11', 2))
    n = int('11', 2)
    n = int('10', 2)
    n = int('1011', 2)
    print(Solution().hammingWeight(n))
