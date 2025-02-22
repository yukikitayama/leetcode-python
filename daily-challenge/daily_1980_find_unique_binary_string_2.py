"""
No need to check more than (n + 1) different binary strings, because nums contains only n strings
  at least one of (n + 1) would not appear in nums
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        for num in range(len(nums) + 1):
            if num not in integers:
                bin_str = bin(num)[2:]

                if len(bin_str) < len(nums):
                    bin_str = "0" * (len(nums) - len(bin_str)) + bin_str

                return bin_str

        return ""

    def findDifferentBinaryString1(self, nums: List[str]) -> str:
        nums_set = set(nums)

        def recursion(comb):

            if len(comb) == len(nums):
                if comb not in nums_set:
                    return comb
                else:
                    return ""

            res = recursion(comb + "0")

            if res:
                return res

            res = recursion(comb + "1")

            return res

        return recursion("")