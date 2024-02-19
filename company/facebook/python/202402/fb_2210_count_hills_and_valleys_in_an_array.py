"""
iterate from left to right
  up boolean
  down boolean
  when up is True and current is smaller than prev, increment hills
    up set False
    down set true
  when down is True and current is bigger than prev, increment valleys
    down set False
    up set True
return sum of hills and valleys counter
"""


class Solution:
    # def countHillValley(self, nums: List[int]) -> int:

    #     hill = 0
    #     valley = 0
    #     up = False
    #     down = False

    #     for i in range(1, len(nums)):

    #         if nums[i] > nums[i - 1]:
    #             if down:
    #                 valley += 1
    #                 down = False
    #                 up = True
    #             else:
    #                 up = True

    #         elif nums[i] < nums[i - 1]:
    #             if up:
    #                 hill += 1
    #                 up = False
    #                 down = True
    #             else:
    #                 down = True

    #     return hill + valley

    # In-place modify to remove duplicated numbers
    def countHillValley(self, nums: List[int]) -> int:

        ans = 0

        for i in range(1, len(nums) - 1):

            # Inplace modify current number with previously seen number to remove duplicates
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i - 1]

            # Hill
            elif nums[i - 1] < nums[i] > nums[i + 1]:
                ans += 1

            # Valley
            elif nums[i - 1] > nums[i] < nums[i + 1]:
                ans += 1

        return ans
