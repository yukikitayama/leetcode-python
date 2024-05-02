"""
result of XOR is 1 when the number of 1 bits is odd and 0 otherwise

The number of bit mismatches is the minimum number of operations required because each bit difference between finalXor and K will require one operation to flip that bit in any of the NNN integers in the array.
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_xor = 0
        for num in nums:
            nums_xor = nums_xor ^ num

        mismatch = nums_xor ^ k

        return bin(mismatch).count("1")

    def minOperations1(self, nums: List[int], k: int) -> int:
        final_xor = 0
        for num in nums:
            final_xor = final_xor ^ num

        print("final_xor", final_xor, bin(final_xor))
        print("k", k, bin(k))

        ans = 0

        # Continue even if one of them is 0
        while k or final_xor:

            # num % 2 typically is used for odd and even number identification
            # but when num is odd, rightmost bit is 1 (2**0 = 1)
            # when num is even, rightmost bit is 0
            # So num % 2 can also be used to identify whether the rightmost bit is 0 or 1
            # This can work even if one of them is 0
            if k % 2 != final_xor % 2:
                ans += 1

            # 5: 101, 5 // 2 = 2: 10
            # 6: 110, 6 // 2 = 3: 11
            # Remove rightmost bit
            # k //= 2
            # final_xor //= 2

            # Rightshift to remove rightmost bit
            k = k >> 1
            final_xor = final_xor >> 1

            # print("final_xor", final_xor, bin(final_xor))
            # print("k", k, bin(k))

        return ans
