from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        # Kadane's algorithm
        # ans is the answer for 1-interval subarrays
        ans = cur = float('-inf')
        for x in nums:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        # rightsums is the cumulative sum from the right
        rightsums = [None] * n
        rightsums[-1] = nums[-1]
        # n - 2 because n - 1 was initialized above
        for i in range(n - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + nums[i]

        # print(f'rightsums: {rightsums}')

        # maxright finds a maximum sum so far from the right
        maxright = [None] * n
        maxright[-1] = rightsums[-1]
        for i in range(n - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])

        # print(f'maxright: {maxright}')

        # i + 2 because if it's i + 1, it becomes one interval, so need space between left and right
        leftsum = 0
        for i in range(n - 2):
            leftsum += nums[i]
            ans = max(ans, leftsum + maxright[i+2])

        return ans


"""
The idea is that first do the kadane's algorithm without worrying about circular feature.
Then if a subarray is circular, you can think there are two subarray, so get the max from two subarray
and compare the two subarray max with the previously calculated kadane's answer.
"""


nums = [1,-2,3,-2]
# nums = [5,-3,5]
# nums = [3,-1,2,-1]
# nums = [3,-2,2,-3]
# nums = [-2,-3,-1]
print(Solution().maxSubarraySumCircular(nums))
