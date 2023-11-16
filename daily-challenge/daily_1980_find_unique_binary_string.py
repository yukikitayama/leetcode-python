from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)

        def generate(curr):

            if len(curr) == n:

                if curr not in nums:
                    return curr

                return ""

            else:

                add_zero = generate(curr + "0")

                if add_zero:
                    return add_zero

                return generate(curr + "1")

        return generate("")


