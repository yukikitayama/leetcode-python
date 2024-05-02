"""
Number of subsequences of an array of length n is 2**n

One approach would be to generate all possible subsequences and compute their bitwise OR. However, this would be computationally expensive, as the number of subsequences grows exponentially with the size of the input array.

The key idea here is that if a bit position has at least one occurrence of a set bit, then that bit should be set in the final result.

When two numbers with set bits at the same position are added, the resulting sum will have the next higher bit position set as well, due to the carry
1 + 1 = 2, 001 + 001 = 010
2 + 2 = 4, 010 + 010 = 100

To capture this property, we need to add half the count of set bits at each position to the next higher position in the counter array. This ensures the result has all the correct bits set.
"""

from typing import List


class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            ans |= num | prefix_sum

            print(
                f"num: {num}, bin(num): {bin(num)}, prefix_sum: {prefix_sum}, bin(prefix_sum): {bin(prefix_sum)}, ans: {ans}, bin(ans): {bin(ans)}")

        return ans

    def subsequenceSumOr1(self, nums: List[int]) -> int:

        # this array left is actually rightmost bit and the array right is leftmost bit
        bit_set_counts = [0] * 64

        for num in nums:

            # print(f"num: {nums}, bin(num): {bin(num)}")

            # 31 because signed 32-bit integer has the last position for sign of pos or neg
            for i in range(31):

                # Identify 1 bit in each bit position from rightmost to leftmost
                if num & (1 << i):
                    bit_set_counts[i] += 1

        # print(bit_set_counts)

        ans = 0

        # 63 because signed 64-bit integer has the last position for sign of pos or neg
        for i in range(63):

            if bit_set_counts[i] > 0:
                # Basci OR operation
                ans |= 1 << i

            # Carry
            # // 2 getting half because 2 1-bits are added and move to the next largest bit
            # half of the counts can go
            bit_set_counts[i + 1] += bit_set_counts[i] // 2

        return ans