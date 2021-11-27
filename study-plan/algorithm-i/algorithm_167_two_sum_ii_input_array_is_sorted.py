"""
Algorithm
- Initialize left to 0 and right to len(numbers) - 1
- While left < right
  - if numbers[left] + numbers[right] == target
    - return [left + 1, right + 1]
  - if the sum is bigger than target
    - decrement right index
  - if the sum is smaller than target
    - increment left index

Complexity
- Time is O(n)
- Space is O(1)
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:

            summed = numbers[left] + numbers[right]

            if summed == target:
                return [left + 1, right + 1]

            elif summed > target:
                right -= 1

            elif summed < target:
                left += 1

        return [-1, -1]


numbers = [2, 7, 11, 15]
target = 9
numbers = [2,3,4]
target = 6
numbers = [-1,0]
target = -1
print(Solution().twoSum(numbers, target))


