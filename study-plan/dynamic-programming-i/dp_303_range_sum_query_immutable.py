from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sums[i + 1] = self.sums[i] + nums[i]

        # print(f'nums: {nums}')
        # print(f'sums: {self.sums}')

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]


nums = [-2, 0, 3, -5, 2, -1]
query = [0, 2]
obj = NumArray(nums)
print(obj.sumRange(*query))
