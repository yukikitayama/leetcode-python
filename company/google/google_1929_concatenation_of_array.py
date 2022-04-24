from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * 2 * n

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans


if __name__ == '__main__':
    nums = [1, 2, 1]
    print(Solution().getConcatenation(nums))
