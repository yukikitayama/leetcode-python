"""
Counting sort
nums = [5,2,3,1]
min: 1
max: 5
count: [1, 1, 1, 0, 1]
5 - 1 = 4
"""

from typing import List
import collections


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter = collections.Counter()
        min_num = min(nums)
        max_num = max(nums)

        for num in nums:
            counter[num] += 1

        i = 0
        for num in range(min_num, max_num + 1):
            while counter[num] > 0:
                nums[i] = num
                counter[num] -= 1
                i += 1

        return nums

    def sortArray1(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)
        count = [0] * (max_num - min_num + 1)
        for num in nums:
            i = num - min_num
            count[i] += 1

        # print(count)

        ans = []
        for i in range(len(count)):
            while count[i] > 0:
                ans.append(i + min_num)
                count[i] -= 1

        return ans
