"""
[1, 2, 3, 5]
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]

            # print(f"left: {left}, right: {right}, sum_: {sum_}")

            if sum_ == target:
                return [left + 1, right + 1]

            elif sum_ < target:
                left += 1

            elif sum_ > target:
                right -= 1