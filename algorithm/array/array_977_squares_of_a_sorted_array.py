from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):

            if abs(nums[left]) > abs(nums[right]):
                curr = nums[left]
                left += 1

            else:
                curr = nums[right]
                right -= 1

            ans[i] = curr ** 2

        return ans


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))
