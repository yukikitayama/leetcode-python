"""
- Maximum sum circular subarray is still maximum subarray sum
  - Use Kadane's Algorithm
- two-interval subarray
  - a0, ... ai + aj, ... an-1
  - Sum of whole array - (ai + 1, ... aj - 1)
"""


from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def kadane(array):
            ans = cur = float('-inf')
            for x in array:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        s = sum(nums)
        if len(nums) == 1:
            return s

        ans1 = kadane(nums)
        # Use Kadane's Algorithm to find max subarray sum
        # By passing negative of the array, finding the minimum sum of the original array
        # By adding minimum sum from the sum of the original array,
        # it removes the subarray which decrease the original sum
        ans2 = s + kadane(-nums[i] for i in range(1, len(nums)))
        ans3 = s + kadane(-nums[i] for i in range(len(nums) - 1))

        # print(f'ans1: {ans1}')
        # print(f'ans2: {ans2}')
        # print(f'ans3: {ans3}')

        return max(ans1, ans2, ans3)


nums = [1,-2,3,-2]
nums = [5,-3,5]
print(Solution().maxSubarraySumCircular(nums))


