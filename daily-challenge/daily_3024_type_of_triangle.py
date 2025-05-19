"""
none
  if one side is bigger than the sum of the other two sides
"""

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:

        if (
            nums[0] >= (nums[1] + nums[2])
            or nums[1] >= (nums[2] + nums[0])
            or nums[2] >= (nums[0] + nums[1])
        ):
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
            return "isosceles"
        else:
            return "scalene"