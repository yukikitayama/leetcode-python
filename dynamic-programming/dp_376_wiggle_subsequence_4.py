"""
Example
nums = [1, 17,  5, 10,13,15,  10, 5, 16, 8]
- diff: [16, -12, 5, 3, 2, -5, -5, 11, -8]
- positive: [1]
- if current diff with previous is negative,
  negative is 1 + previous positive length
  positive current needs to have the previous value
- if current diff with previous is positive
  positive is 1 + previous negative length
  negative current needs to have the previous value
- What is positive diff appear twice
  - nums: [1, 17, 5, 10, 13]
  - diff: [16, -12, 5, 3]
  - positive: [1, _, 3, 3]
  - negative: [_, 2, _, ]
- If the different is 0, not update, so just set the current positive and negative to the previous value

Idea
- We don't have to return the found subsequence
- We just wanna know the length
- If we use dp, dp array can only contains the length
- If the difference between current num and previous num is positive
  and if the previous difference was negative
  - Increment wiggle length
- The opposite is true
-

Algorithm
"""


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        positive = [0] * len(nums)
        negative = [0] * len(nums)

        positive[0] = 1
        negative[0] = 1

        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]

            # Positive
            if curr_diff > 0:
                positive[i] = 1 + negative[i - 1]
                negative[i] = negative[i - 1]

            # Negative
            elif curr_diff < 0:
                negative[i] = 1 + positive[i - 1]
                positive[i] = positive[i - 1]

            # No diff
            else:
                positive[i] = positive[i - 1]
                negative[i] = negative[i - 1]

            # print(f'  curr_diff: {curr_diff}, positive: {positive}, negative: {negative}')

        return max(positive[-1], negative[-1])


"""
Test
nums: [1,7,4,9,2,5]
len(nums): 6
positive: [0, 0, 0, 0, 0, 0]
negative: [0, 0, 0, 0, 0, 0]
i: 1, diff: 6, positive: [0, 1, 0, 0, 0, 0], negative: [0, 0, 0, 0, 0, 0]
i: 2, diff: -3, negative: [0, 0, 2, 0, 0, 0], positive: [0, 1, 1, 0, 0, 0]
i: 3, diff: 5, positive: [0, 1, 1, 3, 0, 0], negative: [0, 0, 2, 2, 0, 0]
i: 4, diff: -7, negative: [0, 0, 2, 2, 4, 0], positive: [0, 1, 1, 3, 3, 0]
i: 5, diff: 3, positive: [0, 1, 1, 3, 3, 5], negative: [0, 0, 2, 2, 4, 4]
max(positive[-1], negative[-1]): 5
"""


nums = [1,7,4,9,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2,3,4,5,6,7,8,9]
print(Solution().wiggleMaxLength(nums))
