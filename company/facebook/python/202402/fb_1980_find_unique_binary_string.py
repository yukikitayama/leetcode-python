"""
Naive
  Use the first element to find n
  generate all the binary string of size n
  make both arrays set
  find one binary string from generated which doesn't appear in given nums
  but it takes time and space

Keep taking XOR
"""

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        # nums_set = set(nums)
        # n = len(nums)

        # def generate(curr):

        #     if len(curr) == n:
        #         if curr not in nums_set:
        #             return curr
        #         else:
        #             return ""

        #     res = generate(curr + "0")

        #     # If not empty is answer
        #     if res:
        #         return res

        #     return generate(curr + "1")

        # return generate("")

        integers = set([int(num, base=2) for num in nums])

        n = len(nums)
        # n: 3, range(n + 1): [0, 1, 2, 3],
        # range(n + 1) can check one more integer than give nums, and that's enough
        for num in range(n + 1):
            if num not in integers:
                bin_str = bin(num)[2:]
                bin_str = (n - len(bin_str)) * "0" + bin_str
                return bin_str
        return ""