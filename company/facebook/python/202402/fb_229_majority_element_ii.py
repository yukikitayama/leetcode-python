"""
Hint
  Think about the possible number of elements that can appear more than ⌊ n/3 ⌋ times in the array.
  Only 2
    [1, 1, 1, 1, 2, 2, 2, 2, 3], 9 / 3 = 3

Boyer-moore voting algorithm
  typically, one counter and one num
  Here, two numbers and two counter
  Both counters are decremented when the current element is different from both
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        num1 = None
        num2 = None
        counter1 = 0
        counter2 = 0

        for i in range(len(nums)):

            if nums[i] == num1:
                counter1 += 1
            elif nums[i] == num2:
                counter2 += 1

            elif counter1 == 0:
                num1 = nums[i]
                counter1 += 1
            elif counter2 == 0:
                num2 = nums[i]
                counter2 += 1

            else:
                counter1 -= 1
                counter2 -= 1

        print(f"num1: {num1}, counter1: {counter1}, num2: {num2}, counter2: {counter2}")

        ans = []

        for num in [num1, num2]:
            if nums.count(num) > len(nums) // 3:
                ans.append(num)

        return ans
