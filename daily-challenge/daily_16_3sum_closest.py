from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):

            low, high = i + 1, len(nums) - 1

            while low < high:

                sum_ = nums[i] + nums[low] + nums[high]

                if abs(target - sum_) < abs(diff):
                    diff = target - sum_

                if sum_ < target:
                    low += 1

                else:
                    high -= 1

            if diff == 0:
                break

        return target - diff


if __name__ == '__main__':
    pass
