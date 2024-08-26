class Solution:
    def findComplement(self, num: int) -> int:
        ans = num
        bitmask = 1
        bit_counter = num

        while bit_counter != 0:

            # XOR with 1 bit flis 0 to 1, 1 to 0
            ans = ans ^ bitmask

            # Move 1-bit bitmask to left
            bitmask = bitmask << 1

            # Track rest of the bit
            bit_counter = bit_counter >> 1

        return ans