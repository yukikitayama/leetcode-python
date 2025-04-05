"""
XOR prefix
nums: [5, 1, 6]
prefix: [5, 4, 2]
"""


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans |= num
        return ans << (len(nums) - 1)

    def subsetXORSum1(self, nums: List[int]) -> int:
        ans = 0

        def recursion(index, curr):
            nonlocal ans
            if index == len(nums):
                ans += curr
                return

            recursion(index + 1, curr ^ nums[index])
            recursion(index + 1, curr)

        recursion(0, 0)

        return ans

    def subsetXORSum1(self, nums: List[int]) -> int:

        subsets = []

        def generate_subsets(index, comb):
            if index == len(nums):
                subsets.append(comb[:])
                return

                # Include
            comb.append(nums[index])
            generate_subsets(index + 1, comb)

            # Exclude
            comb.pop()
            generate_subsets(index + 1, comb)

        generate_subsets(0, [])

        ans = 0

        for subset in subsets:
            xor_total = 0
            for num in subset:
                xor_total ^= num
            ans += xor_total

        return ans