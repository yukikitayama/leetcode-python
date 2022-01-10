"""
- Similar to 67. Add Binary
"""


from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # -2 to remove the length of leading '0b'
        L = len(bin(max(nums))) - 2
        max_xor = 0
        # From the leftmost bit to right most bit
        for i in range(L)[::-1]:
            # print(f'  i: {i}')

            # Go to the next bit by left shift
            max_xor <<= 1
            # Set 1 in the smallest bit
            curr_xor = max_xor | 1

            # print(f'    curr_xor: {curr_xor}, bin: {bin(curr_xor)}')

            # Get ith from the right '0' or/and '1'
            prefixes = {num >> i for num in nums}
            # print('    ', [bin(p) for p in prefixes])

            max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)

            # print(f'    max_xor: {max_xor}, bin: {bin(max_xor)}')

        return max_xor


if __name__ == '__main__':
    a = 5
    b = 25
    # print(a ^ b)
    # print(bin(a))
    # print(bin(b))
    # print(bin(a ^ b))
    nums = [3,10,5,25,2,8]
    print(Solution().findMaximumXOR(nums))

    # i = 4
    # for num in nums:
    #     print(f'num: {num}, bin: {bin(num)}, num >> i: {num >> i}')
