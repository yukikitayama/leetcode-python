from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0

        start = 0

        for end in range(len(nums)):

            if end and nums[end - 1] >= nums[end]:
                start = end

            ans = max(ans, end - start + 1)

        return ans


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    print(Solution().findLengthOfLCIS(nums))
