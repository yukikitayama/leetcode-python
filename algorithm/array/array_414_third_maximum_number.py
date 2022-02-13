"""
- If length less than 3,
  - max()
- Otherwise
  - heap?
"""


from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)

        max_ = max(nums)

        if len(nums) < 3:
            return max_

        nums.remove(max_)
        max_ = max(nums)
        nums.remove(max_)
        max_ = max(nums)
        return max_


if __name__ == '__main__':
    nums = [3, 2, 1]
    print(Solution().thirdMax(nums))
