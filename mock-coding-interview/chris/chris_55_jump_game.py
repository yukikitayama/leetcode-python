"""
no negative
10**4, 10,000, 100,000,000

[2,3,1,1,4]
0: 0 + 1, 0 + 2
  max: 2
1: 1 + 1, .. 1 + 3
  max: 4
2: 2 + 1
  max: 3
3: 3 + 1
  max+ 4

[3,2,1,0,4]
0: 0 + 1, ... 0 + 3
  max: 3
1: 1 + 1, ... 1 + 2
  max: 3
2: 2 + 1
  max: 3
3: 3 + 0
  max: 3
4: max: 3,
  if current index is bigger than max so far,
    invalid
      return False

if current index == len(nums) - 1
  and no invalid experienced
    return True

0 at the 1st element
  [0, 1, 1, 1]
  max_so_far should start with 0
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_so_far = 0
        for i in range(len(nums)):

            if i > max_so_far:
                return False

            if i == len(nums) - 1:
                return True

            max_so_far = max(i + nums[i], max_so_far)

        # return True

