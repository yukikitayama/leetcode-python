"""
Example
- nums: [1, -2, -3, 4]
- dp_positive: [1, 1, 3, 4]
  - 3 because 1 * -2 * -3 = 6
- dp_negative: [0, 1, 1, 1]
  - second 1 because -2 * -3 goes back to positive

Algorithm
- Initialize dp_positive and dp_negative array with 0
  - dp_positive[i] represents the length of positive subarray up to i
  - dp_negative[i] represents the length of negative subarray up to i
- base case
  - if nums[0] is positive, dp_positive[0] = 1
  - if negative, dp_positive[0] = 1
- for each num in nums from second element
  - if it's positive and previous was positive
    - dp_positive[i] = dp_positive[i - 1] + 1
  - if it's positive and previous was negative
    - dp_negative[i] = dp_positive[i - 1] + 1
  - if it's negative and previous was positive
    - dp_negative[i] = dp_positive[i - 1] + 1
  - if it's negative and previous was negative
    - dp_positive[i] = dp_negative[i - 1] + 1
  - if it's zero
    - it resets
    - dp_positive[i] = 0
    - dp_negative[i] = 0
- return max(dp_positive)
"""


from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp_positive = [0] * len(nums)
        dp_negative = [0] * len(nums)

        if nums[0] > 0:
            dp_positive[0] = 1
        elif nums[0] < 0:
            dp_negative[0] = 1
        # if nums[0] is 0, do nothing

        for i in range(1, len(dp_positive)):

            curr_num = nums[i]

            if curr_num > 0:
                dp_positive[i] = dp_positive[i - 1] + 1
                if dp_negative[i - 1] > 0:
                    dp_negative[i] = dp_negative[i - 1] + 1
                # Reset negative length
                else:
                    dp_negative[i] = 0
            elif curr_num < 0:
                dp_negative[i] = dp_positive[i - 1] + 1
                if dp_negative[i - 1] > 0:
                    dp_positive[i] = dp_negative[i - 1] + 1
                else:
                    dp_positive[i] = 0
            elif curr_num == 0:
                # Actually does not below because initialized with 0
                dp_positive[i] = 0
                dp_negative[i] = 0

        # print(f'dp_positive: {dp_positive}')
        # print(f'dp_negative: {dp_negative}')

        return max(dp_positive)


"""
Test
nums: [1,-2,-3,4]
dp_positive: [1, 0, 0, 0]
dp_negative: [0, 0, 0, 0]
i: 1, curr_num: -2, prev_num: 1, dp_negative[i]: dp_positive[i - 1] + 1 = 1 + 1 = 2, 
  dp_negative: [0, 2, 0, 0]
i: 2, curr_num: -3, prev_num: -2, dp_positive[i]: dp_negative[i - 1] + 1 = 2 + 1 = 3,
  dp_positive: [1, 0, 3, 0]
i: 3, curr_num: 4, prev_num: -3, dp_negative[i]: dp_positive[i - 1] + 1 = 3 + 1 = 4,
  dp_negative: [0, 2, 0, 4]
  
Test zero 
nums: [-1,-2,-3,0,1]
dp_positive: [0, 0, 0, 0, 0]
dp_negative: [1, 0, 0, 0, 0]

dp_positive: [0, 2, 0, 0, 0]
dp_negative: [1, 0, 3, 0, 0]
i: 3, curr_num: 0, prev_num: -3, 
"""
nums = [1,-2,-3,4]
nums = [0,1,-2,-3,-4]
nums = [-1,-2,-3,0,1]
nums = [-1,2]
nums = [1,2,3,5,-6,4,0,10]
print(Solution().getMaxLen(nums))

