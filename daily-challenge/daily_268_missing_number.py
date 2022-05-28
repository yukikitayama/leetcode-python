from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)

        for i in range(len(nums) + 1):
            if i not in set_nums:
                return i


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        flag = [False] * (n + 1)

        for i in range(n):
            flag[nums[i]] = True

        for i, f in enumerate(flag):
            if not f:
                return i


if __name__ == '__main__':
    nums = [3, 0, 1]
    nums = [0, 1]
    print(Solution().missingNumber(nums))
