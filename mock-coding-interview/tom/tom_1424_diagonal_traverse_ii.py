from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        id_to_nums = collections.defaultdict(list)
        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                id_to_nums[r + c].append(nums[r][c])

        ans = []
        id_ = 0
        while id_ in id_to_nums:
            ans.extend(id_to_nums[id_])
            id_ += 1
        return ans

    def findDiagonalOrder1(self, nums: List[List[int]]) -> List[int]:

        id_to_nums = collections.defaultdict(list)
        for r, row in enumerate(nums):
            for c in range(len(row)):
                id_ = r + c
                id_to_nums[id_].append(nums[r][c])

        # print(id_to_nums)

        ans = []
        for k, v in id_to_nums.items():
            v.reverse()
            ans.extend(v)

        return ans