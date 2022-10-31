from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0
        ans = 1 if len(nums) else 0
        num_zero = 1 if nums[0] == 0 else 0

        while right < len(nums) and left < len(nums):

            while num_zero < 2:

                # print(f'In right, left: {left}, right: {right}')

                right += 1

                if right == len(nums):
                    break
                elif nums[right] == 0:
                    num_zero += 1

                if num_zero < 2:
                    ans = max(ans, right - left + 1)

            while num_zero == 2:

                # print(f'In left, left: {left}, right: {right}')

                if nums[left] == 0:
                    num_zero -= 1
                left += 1

        return ans


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0]
    # 4
    nums = [1, 0, 1, 1, 0, 1]
    # 4
    print(Solution().findMaxConsecutiveOnes(nums))
