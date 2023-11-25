"""
There will be duplicated computations if simply doing all the combinations
Use hashmap of key pair of indices and value absolute difference
"""

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sums = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])

        n = len(nums)

        ans = []

        for i in range(n):

            sum_left = prefix_sums[i] - nums[i]
            sum_right = prefix_sums[-1] - prefix_sums[i]

            count_left = i
            count_right = n - 1 - i

            total_left = count_left * nums[i] - sum_left
            total_right = sum_right - count_right * nums[i]

            ans.append(total_left + total_right)

        return ans


class SolutionOptimized:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)

        left = 0
        ans = []
        for i in range(n):
            right = total - left - nums[i]
            l_c = i
            r_c = n - i - 1
            l_t = l_c * nums[i] - left
            r_t = right - r_c * nums[i]

            ans.append(l_t + r_t)

            left += nums[i]

        return ans


if __name__ == "__main__":
    nums = [2, 3, 5]
    nums = [1, 4, 6, 8, 10]
    print(Solution().getSumAbsoluteDifferences(nums))
    print(SolutionOptimized().getSumAbsoluteDifferences(nums))
