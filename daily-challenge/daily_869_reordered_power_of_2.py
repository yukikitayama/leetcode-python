import itertools


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        for candidate in itertools.permutations(str(n)):
            num = int(''.join(candidate))
            # print(num)
            bin_str = bin(num)
            # print(bin_str)

            # If not leading 0, and
            # If a number is power of 2, binary representation should only contains one 1
            if candidate[0] != '0' and bin_str.count('1') == 1:
                return True

        return False


if __name__ == '__main__':
    n = 123
    n = 16
    n = 32
    print(Solution().reorderedPowerOf2(n))
