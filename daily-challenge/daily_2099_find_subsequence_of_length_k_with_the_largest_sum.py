from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indices_nums = [[i, num] for i, num in enumerate(nums)]
        indices_nums.sort(key=lambda x: -x[1])
        indices_nums = sorted(indices_nums[:k])
        return [num for i, num in indices_nums]

    def maxSubsequence1(self, nums: List[int], k: int) -> List[int]:
        indices_nums = [(i, num) for i, num in enumerate(nums)]
        indices_nums.sort(key=lambda x: (x[1], x[0]))
        indices_nums = indices_nums[-k:]
        indices_nums.sort(key=lambda x: (x[0], x[1]))
        ans = [num for i, num in indices_nums]
        return ans