"""
- binary search
  - if current num is larger than target
    - 3, 4, 5, 0, 1, 2
    - current num: 1, target: 0
    - right = mid - 1
  - if current num is smaller than target
    - current num: 1, target: 5
    -

- Worst case
  - nums: [1, 1, 1, 1, 1], target: 2
- Best case
  - all the elements in nums are distinct


- 1. mid in first, and target in second
  - (mid, right]
- 2. mid in second, and target in first
  - [left, mid)
- 3. mid and target in the same array
  - 3-1. if mid is smaller than target, (mid, right]
  - 3-2. if mid is bigger than target, [left, mid)
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        def is_binary_search_helpful(nums, left, num_in_mid):
            return nums[left] != num_in_mid

        def does_num_exist_in_first(nums, left, num):
            # nums is rotated and sorted
            # first nums is greater than or equal to the second nums
            # if the num is bigger than the small element (left pointer) in the first nums,
            # the num exists in the first nums,
            # because the second nums are all smaller than or equal to first nums
            return nums[left] <= num

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if not is_binary_search_helpful(nums, left, nums[mid]):
                left += 1
                continue

            mid_in_first = does_num_exist_in_first(nums, left, nums[mid])

            target_in_first = does_num_exist_in_first(nums, left, target)

            # If mid and target belong to the different arrays
            if mid_in_first ^ target_in_first:
                if mid_in_first:
                    left = mid + 1
                else:
                    right = mid - 1

            # If both mid and target together belong to the first or the second
            # This is easy because we can do binary search
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        # If the while loop cannot return true, the target does not exist
        return False


nums = [2,5,6,0,0,1,2]
target = 0
nums = [2,5,6,0,0,1,2]
target = 3
print(Solution().search(nums, target))
