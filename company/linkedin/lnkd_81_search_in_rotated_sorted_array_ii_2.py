"""
- if nums[mid] is equal to nums[left], then nums[mid] might belong to
  the first array or the second array. We can't use binary search this case
  - just increment left pointer
- This makes worst case time O(n), instead of O(logn) even with binary search implemented
  - The worst case is when all the element are the same, and target does not exist in nums
- The best case when all the elements are unique, so divide search space into half and time O(logn)
- What would happend if nums have duplicates?
  - Miss opportunity to use binary search
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid]:
                left += 1
                continue

            # mid and left are in the same increasing subarray
            # e.g. 4(left), 5, 6, 7(mid), 1, 2, 3
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # mid and left are not in the same increasing subarray
            # 4(left), 5, 6, 1(mid), 2, 3
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


nums = [2,5,6,0,0,1,2]
target = 0
nums = [2,5,6,0,0,1,2]
target = 3
print(Solution().search(nums, target))
