# print(bin(3))
# print(bin(1))

# print(bin(1))
# print(bin(4))


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Get the positions at which the corresponding bits are different
        xor = x ^ y
        distance = 0

        # As long as there's at least one 1
        while xor:

            # print(f'xor & 1: {xor & 1}, bin(xor): {bin(xor)}')

            # If the rightmost bit is 1
            if xor & 1:
                distance += 1

            # Move one bit to right
            xor = xor >> 1

        return distance


"""
Complexity
- Time
  - There's a while loop, but Python integer is 32 bit, so it takes at most 32 iteration
  - It means time is O(32) = O(1)
"""


print(Solution().hammingDistance(1, 4))

