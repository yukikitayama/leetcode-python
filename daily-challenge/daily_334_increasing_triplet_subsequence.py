"""
- length more than 2
- 2 pointers
- Iterate from left and right
"""


from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for num in nums:

            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


if __name__ == '__main__':
    pass
