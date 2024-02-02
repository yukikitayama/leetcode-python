"""
- One pass
- reversed flag
"""


from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        previous = float('-inf')
        flag = False

        for i in range(len(nums)):

            # print(f'num: {nums[i]}')

            if nums[i] > previous:
                previous = nums[i]

            elif nums[i] <= previous:

                if flag:
                    return False

                flag = True
                # We can update previous as long as current is bigger than the element after removing
                if i <= 1 or nums[i - 2] < nums[i]:
                    previous = nums[i]

        return True


if __name__ == '__main__':
    nums = [1, 2, 10, 5, 7]
    nums = [2, 3, 1, 2]
    print(Solution().canBeIncreasing(nums))
