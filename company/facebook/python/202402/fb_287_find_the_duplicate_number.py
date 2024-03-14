"""
[1, 3, 4, 2, 2]
  1: 0
  3: 1
  4: 2
  2: [3, 4]
[1, 2, 3, 4, 5]

Use (num - 1) as index, and supposed to visit element once

bitmask?
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast = nums[0]
        slow = nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast
