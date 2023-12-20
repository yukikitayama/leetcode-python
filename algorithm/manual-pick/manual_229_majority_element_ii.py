"""
Implement Boyer-Moore voting algorithm
"""

from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) / 3
        counter = collections.Counter(nums)
        ans = []
        for k, v in counter.items():
            if v > threshold:
                ans.append(k)
        return ans


class SolutionOpt:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count_1 = 0
        count_2 = 0
        candidate_1 = None
        candidate_2 = None

        for num in nums:

            if num == candidate_1:
                count_1 += 1

            elif num == candidate_2:
                count_2 += 1

            elif count_1 == 0:
                candidate_1 = num
                count_1 += 1

            elif count_2 == 0:
                candidate_2 = num
                count_2 += 1

            else:
                count_1 -= 1
                count_2 -= 1

        ans = []

        for c in [candidate_1, candidate_2]:
            if nums.count(c) > len(nums) // 3:
                ans.append(c)

        return ans


if __name__ == "__main__":
    nums = [3, 2, 3]
    # nums = [1]
    # nums = [1, 2]
    print(SolutionOpt().majorityElement(nums))
