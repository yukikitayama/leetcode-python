from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int):

        def binary_search(nums, target):
            idx = bisect.bisect_left(nums, target)

            if idx == len(nums) or nums[idx] != target:
                return -1

            else:
                return idx

        return binary_search(nums, target)


nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2
print(Solution().search(nums, target))
