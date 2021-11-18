"""
- Treat numbers in array as indices
- Using the indices to mark which numbers appeared and which are missing
"""


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # -1 because nums are 1-based, but index for array is 0-based
            # abs() because even if constraints says nums[i] is positive,
            # in iteration, we mark it negative, so for the next time iterated.
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # +1 because index is 0-based, but the number we need to return is 1-based
                ans.append(i + 1)
        return ans


"""
Complexity
- Time is O(n) to iterate two times
- Space is O(1) because we modify input and exclude the returned answer list 
"""


nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))




