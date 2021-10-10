"""
Top down dp
"""


from typing import List
from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def combs(remain):

            if remain == 0:
                return 1

            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combs(remain - num)

            return result

        return combs(target)


"""
Test
nums: [1, 2, 3]
target: 4
remain: 4, if1: F, result: 0, num: 1, remain - num: 3, if2: T, combs(3)
  remain: 3, if1: F, result: 0, num: 1, remain - num: 2, if2: T, combs(2)
    remain: 2, if1: F, result: 0, num: 1, remain - num: 1, if2: T, combs(1)
      remain: 1, if1: F, result: 0, num: 1, remain - num: 0, if2: T, combs(0)
        remain: 0, if1: T, return 1
      combs(0): 1, result: 1, num: 2, remain - num: -1, if2: F,
        num: 3, remain - num: -2, if2: F, return result: 1
    combs(1): 1, result: 1, num: 2, remain - num: 0, if2: T, combs(0): 1, result: 2
      num: 3, remain - num: -1, if2: F, return result: 2,
  combs(2): 2, result: 1, num: 2, remain - num: 1, if2: T, combs(1): 1, result: 3
    num: 3, remain - num: 0, if2: T, combs(0): 1, result: 4, return result: 4
combs(3): 4, result: 4, num: 2, remain - num: 2, combs(2): 2, result: 6, 
  num: 3, remain - num: 1, combs(1): 1, result: 7, return result: 7
        
memo:
  combs(0): 1
  combs(1): 1
  combs(2): 2
  combs(3): 4
"""


nums = [1,2,3]
target = 4
print(Solution().combinationSum4(nums, target))
