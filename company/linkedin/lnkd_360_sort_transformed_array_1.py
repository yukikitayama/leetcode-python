"""
- When a is positive, min at the slop 0, convex
- When a is negative, max at the slop 0, concave
- The given nums is sorted
- the formula is quadratic
  - When a is positive, min is in the middle
  - When a is negative, min is left and right edges
- After transformation, in absolute, bigger number are at edges
- When a is positive
  - Edge numbers are big
  - Fill ans from the end
  - Set index to the end index of nums
  - Compare num at left and num at right
  - Append bigger element to end of ans
    - If left num is bigger, increment left
    - If right num is bigger, decrement right
- When a is negative
  - Edge numbers are small
  - Fill ans from start
  - Set index to the start index of nums
  - Compare num
"""


from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        print(f'nums: {nums}, a: {a}, b: {b}, c: {c}')

        def transform(x):
            return a * x**2 + b * x + c

        nums = [transform(num) for num in nums]

        print(f'transformed: {nums}')

        ans = [0] * len(nums)

        left, right = 0, len(nums) - 1

        print(f'left: {left}, right: {right}')

        # If a is negative, smallest element should be edges
        i, d = (left, 1) if a < 0 else (right, -1)

        print(f'i: {i}, d: {d}')

        while left <= right:

            print(f'  i: {i}, left: {left}, right: {right}, ')

            if nums[left] * -d > nums[right] * -d:
                ans[i] = nums[left]
                left += 1

            else:
                ans[i] = nums[right]
                right -= 1

            i += d

        return ans


nums = [-4, -2, 2, 4]
a = 1
b = 3
c = 5
nums = [-4,-2,2,4]
a = -1
b = 3
c = 5
print(Solution().sortTransformedArray(nums, a, b, c))

