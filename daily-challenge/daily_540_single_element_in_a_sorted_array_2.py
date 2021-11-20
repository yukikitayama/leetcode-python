"""
- single element is at the first even index not followed by pair
  - If all the numbers are double duplicates, each starts at even index
    and followed by its pair, but single number destroys this property
    - All the pairs before single number have this property
    - But the paris after single number don't
"""


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:

            mid = lo + (hi - lo) // 2

            # If mid is not even, adjust it to be even
            if mid % 2 == 1:
                mid -= 1

            # if the right next is its pair, it means that single number
            # does not appear to the left to destroy first pair at even property
            # so search to right
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2

            # If mid index is odd, the single number somewhere before mid
            # destroys the first pair at even property, so single number is to the left
            else:
                hi = mid


