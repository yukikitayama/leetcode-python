"""
- Do binary search twice
  - First find lower bound
  - Second find upper bound
- If lower bound not found, return [-1, -1]
"""


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_bound(is_first):
            begin = 0
            end = len(nums) - 1

            while begin <= end:

                mid = (begin + end) // 2

                # print(f'begin: {begin}, mid: {mid}, end: {end}')

                if nums[mid] == target:
                    if is_first:
                        if mid == begin or nums[mid - 1] != target:
                            return mid
                        else:
                            end = mid - 1
                    elif not is_first:
                        if mid == end or nums[mid + 1] != target:
                            return mid
                        else:
                            begin = mid + 1

                elif nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    begin = mid + 1

            return -1

        lower_bound = find_bound(True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = find_bound(False)

        return [lower_bound, upper_bound]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    nums = []
    target = 0
    print(Solution().searchRange(nums, target))

