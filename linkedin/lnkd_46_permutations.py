"""
- swap
- iterate index in nums

Complexity
- k-permutations of n, arrangements of k elements from set n, variations, arrangements
  - nPk, Pnk, P(n, k)
  - = n * (n - 1) * (n - 2) * ... * (n - k + 1)
  - n! / (n - k)!
- Time is sum from k=1 to n P(n, k)
"""


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(curr, index):

            # print(f'  in backtracking, curr: {curr}, index: {index}')

            if index == len(nums):
                ans.append(curr[:])
                return

            if index > len(nums):
                return

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]

                backtracking(nums, index + 1)

                nums[i], nums[index] = nums[index], nums[i]

        backtracking(nums, 0)

        return ans


nums = [1,2,3]
nums = [0, 1]
nums = [1]
print(Solution().permute(nums))



