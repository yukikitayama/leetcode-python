"""
Idea
- The given nums is ascending order
- We need special treatment only when a is positive,
  - because after transformation, the number becomes big, but we are required to make
    ascending order list, which starts from the small number
- After transformation
  - If a is positive, big numbers are at the edge
  - If a is negative, small numbers are at the edge
- Use two pointers of start index and end index
  - We need to make ascending order answer list
  - If a is positive, fill answers from the end
    - Compare, in transformed nums, nums[left] with nums[right]
      - Append a bigger number to answer list
  - Else, fill answers from the start
    - Compare nums[left] with nums[right]
      - Append smaller number to answer list
- Background of the else
  - When a is negative, the edge numbers are small numbers,
    so it's safe to append smaller to start at the answer list
  - When a is 0, the number becomes bx + c, but it just fills the smaller number
    in the start of answer list anyway
  - So we only append from the end when a is positive, because the numbers it currently
    looks at by left and right indices are the big numbers

Complexity
- Let n be the length of nums
- Time is O(n) because while loop ends in n
- Space is O(1) by excluding nums and ans
"""


from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(x):
            return a * x**2 + b * x + c

        nums = [transform(num) for num in nums]

        ans = [0] * len(nums)

        left, right = 0, len(nums) - 1

        if a > 0:
            i = right
        else:
            i = left

        while left <= right:

            left_num = nums[left]
            right_num = nums[right]

            if a > 0:
                if left_num > right_num:
                    ans[i] = left_num
                    left += 1
                else:
                    ans[i] = right_num
                    right -= 1
                i -= 1

            else:
                if left_num > right_num:
                    ans[i] = right_num
                    right -= 1
                else:
                    ans[i] = left_num
                    left += 1

                i += 1

        return ans


nums = [-4, -2, 2, 4]
a = 1
b = 3
c = 5
nums = [-4,-2,2,4]
a = -1
b = 3
c = 5
nums = [-4, -2, 2, 4]
a = 0
b = 3
c = 5
print(Solution().sortTransformedArray(nums, a, b, c))

