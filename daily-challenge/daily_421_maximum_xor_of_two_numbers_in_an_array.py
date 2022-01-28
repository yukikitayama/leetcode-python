"""
- bitwise trie
"""


from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        l = len(bin(max(nums))) - 2

        list_of_list_of_bits = []
        for num in nums:
            bits = []
            for i in range(l):
                bit = (num >> i) & 1
                bits.append(bit)
            list_of_list_of_bits.append(bits[::-1])

        # print(list_of_list_of_bits)
        nums = list_of_list_of_bits

        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0

            for bit in num:

                if not bit in node:
                    node[bit] = {}
                node = node[bit]

                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    # Maximize by adding 1-bit
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    # Cannot maximize, so add 0-bit
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)

        return max_xor


if __name__ == '__main__':
    nums = [3, 10, 5, 25, 2, 8]
    print(Solution().findMaximumXOR(nums))
