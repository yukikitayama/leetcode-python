from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # Why i - 1 != i?
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]) -> None:
        lo = i + 1
        hi = len(nums) - 1

        while lo < hi:
            summed = nums[i] + nums[lo] + nums[hi]
            if summed < 0:
                lo += 1
            elif summed > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


"""
Time complexity
Sorting nums: O(nlogn), twoSumII: O(n), threeSum uses twoSumII uses twoSumII n times
so O(nlogn) + O(n**2) = O(n**2)

Space complexity
We ignore the memory required for the output, sorting spends O(logn) or O(n)
"""



nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
