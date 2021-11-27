"""
- Store a permutation is set, so it can keep only unique permutations
- When we return the answer, convert set of lists into list of lists
- Backtracking
- Time is P(n, k)
"""


from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutation_set = set()

        def backtracking(index):
            if index == len(nums):
                permutation_set.add(tuple(nums[:]))

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]

                backtracking(index + 1)

                nums[i], nums[index] = nums[index], nums[i]

        backtracking(0)

        return [list(permutation) for permutation in permutation_set]


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))






