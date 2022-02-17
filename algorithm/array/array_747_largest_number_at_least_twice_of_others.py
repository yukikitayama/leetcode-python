from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = 0
        second = 0

        for i in range(len(nums)):

            if nums[i] >= first:
                second = first
                first = nums[i]
                idx = i
            elif nums[i] >= second:
                second = nums[i]

        if first >= second * 2:
            return idx
        else:
            return -1


if __name__ == '__main__':
    nums = [3, 6, 1, 0]
    nums = [1, 2, 3, 4]
    print(Solution().dominantIndex(nums))
