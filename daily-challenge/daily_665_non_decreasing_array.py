"""
- Use stack
- Largest so far
"""


from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num_violations = 0

        for i in range(1, len(nums)):

            if nums[i - 1] > nums[i]:

                if num_violations == 1:
                    return False

                num_violations += 1

                if i == 1 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True


if __name__ == '__main__':
    nums = [4, 2, 3]
    nums = [4, 2, 1]
    print(Solution().checkPossibility(nums))
