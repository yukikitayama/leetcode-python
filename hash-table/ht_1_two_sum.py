from typing import List
import collections


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = collections.defaultdict(int)
        for i, num in enumerate(nums):

            if target - num in num_to_index:
                return [i, num_to_index[target - num]]

            num_to_index[num] = i


"""
- Time is O(n) for the for loop
- Space is O(n) for the hashmap
"""


nums = [2, 7, 11, 15]
target = 9
nums = [3,2,4]
target = 6
nums = [3,3]
target = 6
print(Solution().twoSum(nums, target))




