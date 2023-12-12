"""
Counting sort?
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nums.sort()

        return (nums[-1] - 1) * (nums[-2] - 1)


class SolutionOpt:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
        return (biggest - 1) * (second_biggest - 1)


if __name__ == "__main__":
    nums = [3, 4, 5]
    print(Solution().maxProduct(nums))
    print(SolutionOpt().maxProduct(nums))


