from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        max_1 = float("-inf")
        max_2 = float("-inf")
        min_1 = float("inf")
        min_2 = float("inf")

        for num in nums:

            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_2 = num

            if num < min_1:
                min_2 = min_1
                min_1 = num
            elif num < min_2:
                min_2 = num

        return (max_1 * max_2) - (min_1 * min_2)


if __name__ == "__main__":
    nums = [5, 6, 2, 7, 4]  # 34
    nums = [4, 2, 5, 9, 7, 4, 8]  # 64
    print(Solution().maxProductDifference(nums))
