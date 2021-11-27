"""
- Binary search twice
"""


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_bound(nums, target, is_first):
            n = len(nums)
            begin = 0
            end = n - 1
            while begin <= end:
                mid = begin + (end - begin) // 2

                if nums[mid] == target:

                    if is_first:
                        if mid == begin or nums[mid - 1] < target:
                            return mid
                        end = mid - 1

                    else:
                        if mid == end or nums[mid + 1] > target:
                            return mid
                        begin = mid + 1

                elif nums[mid] > target:
                    end = mid - 1
                else:
                    begin = mid + 1

            return -1

        lower_bound = find_bound(nums, target, True)
        # If it cannot even find the first index, the target
        # does not exist in nums, so there's no last index either
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = find_bound(nums, target, False)
        return [lower_bound, upper_bound]


nums = [5, 7, 7, 8, 8, 10]
target = 8
# nums = [5,7,7,8,8,10]
# target = 6
# nums = []
# target = 0
# nums = [2,2]
# target = 3
print(Solution().searchRange(nums, target))


