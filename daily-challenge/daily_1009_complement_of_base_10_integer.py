import math


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        num_digit = math.floor(math.log2(n)) + 1
        # print(num_digit)
        one_bit_mask = (1 << num_digit) - 1
        # print(bin(one_bit_mask))
        ans = n ^ one_bit_mask
        # print(bin(ans))
        return ans


if __name__ == '__main__':
    n = 5
    n = 7
    n = 10
    print(Solution().bitwiseComplement(n))