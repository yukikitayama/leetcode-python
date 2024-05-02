"""
[10, 10, 10, 20]

[1, 1, 1, 2] <- assume
or
[1, 1, 1, 4]
"""

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        sorted_arr = sorted(arr)
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in ranks:
                ranks[sorted_arr[i]] = len(ranks) + 1

        ans = []
        for i in range(len(arr)):
            ans.append(ranks[arr[i]])
        return ans

    def arrayRankTransform1(self, arr: List[int]) -> List[int]:
        nums = list(set(arr))
        nums.sort()
        num_to_rank = {}
        for i in range(len(nums)):
            num_to_rank[nums[i]] = i + 1

        ans = []
        for i in range(len(arr)):
            ans.append(num_to_rank[arr[i]])

        return ans
