"""
- brute force by 3 for loops and if sum is 0
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # O(nlogn)
        nums.sort()

        # O(n)
        for i in range(len(nums)):

            # print(f'i: {i}')

            # Break because the numbers after the current num is bigger so that
            # it cannot make sum 0
            if nums[i] > 0:
                break

            # Avoid index out of bound and duplicate
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)

        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]) -> None:
        low, high = i + 1, len(nums) - 1

        while low < high:

            sum = nums[i] + nums[low] + nums[high]

            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                # skip duplicate
                while low < high and nums[low] == nums[low - 1]:
                    low += 1


nums = [-1,0,1,2,-1,-4]
nums = []
nums = [0]
print(Solution().threeSum(nums))

