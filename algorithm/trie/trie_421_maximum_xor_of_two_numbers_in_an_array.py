"""
- To maximize XOR, choose the opposite bit at each step whenever possible
"""


from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        L = len(bin(max(nums))) - 2

        # Zero left-padding
        # (x >> i) & 1 is getting the rightmost bit one by one
        # but we need to [::-1] to reverse it because we got one by one in a reverse order
        # e.g. 5 -> 11001, i: 0, 5 >>
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]

        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0

            # Get a bit from the left
            # Here num is a list of bits, zero left padded
            for bit in num:

                # Insert into Trie
                if not bit in node:
                    node[bit] = {}

                # Search in Trie
                node = node[bit]

                # To maximize XOR, choose the opposite bit at each step whenever possible
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    # As long as opposite bit exist, we can go maximize bit which should be add 1-bit
                    curr_xor = (curr_xor << 1) | 1
                    # Go down the trie further
                    xor_node = xor_node[toggled_bit]

                else:
                    curr_xor <<= 1
                    # toggled_bit does not exist, so
                    # just use the same bit to go down the trie further
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)

        return max_xor


if __name__ == '__main__':
    nums = [3, 10, 5, 25, 2, 8]
    print(Solution().findMaximumXOR(nums))

    # l = len(bin(25)) - 2
    # binaries = []
    # for i in range(l):
    #     # print(f'i: {i}, bin(25 >> i): {bin(25 >> i)}, (25 >> i) & 1: {(25 >> i) & 1}')
    #     # binaries.append((25 >> i) & 1)
    #     print(f'i: {i}, bin(3 >> i): {bin(3 >> i)}, (3 >> i) & 1: {(3 >> i) & 1}')
    #     binaries.append((3 >> i) & 1)
    # # Reverse it because we store bit from the right, but we wanna see bits from the left
    # binaries.reverse()