from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    # target = 5
    target = 2
    print(Solution().searchInsert(nums, target))

