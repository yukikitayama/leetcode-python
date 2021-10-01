from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        n = len(nums)

        def kadane(nums):
            cur = ans = nums[0]
            for num in nums[1:]:
                cur = max(num, cur + num)
                ans = max(ans, cur)
            return ans

        candidate_1 = kadane(nums)
        # kadane(-nums) does not work because it could make the same array as kadane(nums) after subtracting min
        candidate_2 = sum(nums) + kadane([-num for num in nums[0:n - 1]])
        candidate_3 = sum(nums) + kadane([-num for num in nums[1:]])

        # print(f'candidate_1: {candidate_1}, '
        #       f'candidate_2: {candidate_2}, '
        #       f'candidate_3: {candidate_3}')

        return max(candidate_1, candidate_2, candidate_3)


"""
We have nums array. kadane(nums) gives us the maximum of subarray.
Take negative of each num in nums. kadane(-nums) still gives us the max of negative subarray.
It is actually minimum subarray in the origin array multiplied by -1
so -1 * kadane(-nums) is minimum of subarray
so if we get total of nums and subtract minimum of subarray, we can get maximum of subarray
Thus, sum_of_nums - (-1 * kadane(-nums)) = sum_of_nums + kadane(-nums)
"""


# nums = [1,-2,3,-2]
nums = [5,-3,5]
# nums = [3,-1,2,-1]
# nums = [3,-2,2,-3]
# nums = [-2,-3,-1]
# nums = [2, 3, 1]
print(Solution().maxSubarraySumCircular(nums))
