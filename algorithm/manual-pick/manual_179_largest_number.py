"""
Most significant digits should be occupied by the largest digits
"""

from typing import List


class CustomComparisonStr(str):
    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        str_nums = [str(num) for num in nums]
        str_nums.sort(key=CustomComparisonStr, reverse=True)

        print(str_nums)

        ans = "".join(str_nums)

        return "0" if ans[0] == "0" else ans


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))


