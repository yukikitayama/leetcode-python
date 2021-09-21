from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # + 1 because in this problem maxRobbedAmount[n] handles no house case
        # maxRobbedAmount[0] is for all the houses
        # maxRobbedAmount[n] is for no house
        # maxRobbedAmount[n - 1] is for robbing only one hous
        maxRobbedAmount = [0 for _ in range(len(nums) + 1)]
        n = len(nums)

        # Base case
        maxRobbedAmount[n] = 0
        maxRobbedAmount[n - 1] = nums[n - 1]

        # DP table calculation
        # From the end to 0 by step -1
        for i in range(n - 2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

            # print(f'i: {i}, maxRobbedAmount: {maxRobbedAmount}')

        return maxRobbedAmount[0]


"""
Dynamic programming 

Time complexity
Let n be the length of nums. O(n) to iterate for loop

Space complexity
O(n) for dynamic programming table.
"""


nums = [1, 2, 3, 1]
# nums = [2,7,9,3,1]
print(Solution().rob(nums))

