class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        power = 31

        while n:
            # (n & 1) gets the rightmost bit, either 0 or 1
            # << power moves the bit, either 0 or 1, to the left most
            ans += (n & 1) << power

            # Move all the bits to right
            n = n >> 1

            # Decrement power to move to the next left most bit
            power -= 1

        return ans
