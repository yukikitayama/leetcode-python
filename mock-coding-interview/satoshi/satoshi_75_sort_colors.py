"""
[2, 0, 1]
 |

[1, 0, 2]
    |

[0, 1, 2]

[0, 1, 2]
       |
p_zero: 1
p_two: 1

[0, 2, 1]
"""

from typing import List
import collections


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p_zero = 0
        p_two = len(nums) - 1
        i = 0

        while i <= p_two:

            if nums[i] == 0:
                nums[p_zero], nums[i] = nums[i], nums[p_zero]
                p_zero += 1
                i += 1

            elif nums[i] == 2:
                nums[p_two], nums[i] = nums[i], nums[p_two]
                p_two -= 1
                # Don't increment i, because swapping might give us 0 to i, and at the next iteration we wanna move this 0

            # 1
            else:
                i += 1

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        2 passes, S: O(3) -> O(1), {0: 2, 1: 2, 2: 2}
        """
        counter = collections.Counter(nums)

        i = 0
        for k in [0, 1, 2]:
            if k in counter:
                for _ in range(counter[k]):
                    nums[i] = k
                    i += 1