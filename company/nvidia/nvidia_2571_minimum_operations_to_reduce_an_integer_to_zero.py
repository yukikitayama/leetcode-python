"""
bit manipulation?

We can minimize operation when in binary representation, there are consecutive 1-bits
e.g. when 1111 in binary rep, subtract power of 2 requires 4 times
but if we add 2**0 = 1 to 1111, it becomes 10000, then subtract 2**4, then get 0m so only 2 operations
"""


class Solution:
    def minOperations(self, n: int) -> int:

        ans = 0
        count = 0

        for i in range(32):

            # Count 1-bit from right
            if n & (1 << i):
                count += 1

            # If 0-bit
            else:

                # If consecutive
                if count > 1:
                    ans += 1
                    # As if we add 1 to the binary representation so far
                    # so all the 1s so far become 0 and current 0-bit becomes 1
                    count = 1

                # When consecutive didn't occur but there was only one 1-bit
                elif count == 1:
                    ans += 1
                    # Just reset
                    count = 0

        return ans




