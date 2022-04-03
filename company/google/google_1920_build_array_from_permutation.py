from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans


if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    # [0, 1, 2, 4, 5, 3]
    print(Solution().buildArray(nums))
