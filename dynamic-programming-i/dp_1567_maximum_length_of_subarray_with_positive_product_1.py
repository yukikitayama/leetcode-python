from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # Record the maximum length of positive and negative products until the index in array
        pos = [0] * len(nums)
        neg = [0] * len(nums)

        # Initialize base case
        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1

        answer = pos[0]

        for i in range(1, len(nums)):

            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                # Multiplying negative number by positive number does not change sign,
                # so increment neg as well
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]

            # If statement for nums[i]: 0 is not necessary
            # because the below can take care of 0 case
            # pos[i] is not updated by the above two if statements,
            # so initial pos[i] is 0
            answer = max(answer, pos[i])

        return answer


"""
Algorithm


"""

# nums = [1,-2,-3,4]
# nums = [0,1,-2,-3,-4]
# nums = [-1,-2,-3,0,1]
# nums = [-1,2]
nums = [1,2,3,5,-6,4,0,10]
print(Solution().getMaxLen(nums))

