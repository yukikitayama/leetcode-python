class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, n: int) -> int:
        nums = [0] * n
        for i in range(1, n + 1):
            nums[i - 1] = i

        # print(f'nums: {nums}')

        self.permute(nums, 0)

        return self.count

    def permute(self, nums, l):

        # When l exceeds len(nums) - 1, all the integers in the nums permutations satisfies the divisible condition
        if l == len(nums):
            self.count += 1

        for i in range(l, len(nums)):
            self.swap(nums, i, l)

            # Check the current integer meets the divisible condition one by one
            # +1 because integer starts from 1, not 0
            if nums[l] % (l + 1) == 0 or (l + 1) % nums[l] == 0:
                self.permute(nums, l + 1)

            self.swap(nums, i, l)

    def swap(self, nums, x, y):
        nums[x], nums[y] = nums[y], nums[x]


print(Solution().countArrangement(2))
