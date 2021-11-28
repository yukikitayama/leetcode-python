"""
Example
avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 32 / 7 = 4.57... = 4
avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 34 / 7 = 4.85... = 4

Idea
- Calculate prefix sum


"""


from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # print(f'prefix_sum: {prefix_sum}')

        ans = [-1] * len(nums)
        for i in range(k, len(nums) - k):
            # print(f'i: {i}, prefix_sum[i + k + 1]: {prefix_sum[i + k + 1]}')
            total = prefix_sum[i + k + 1] - prefix_sum[i - k]
            # print(f'total: {total}')
            ans[i] = int(total / (2 * k + 1))

        return ans


nums = [7,4,3,9,1,8,5,2,6]
k = 3
nums = [100000]
k = 0
nums = [8]
k = 100000
print(Solution().getAverages(nums, k))

# nums = [7,4,3,9,1,8,5,2,6]
# prefix_sum = [0] * (len(nums) + 1)
# for i in range(len(nums)):
#     prefix_sum[i + 1] = prefix_sum[i] + nums[i]
# print(f'prefix_sum: {prefix_sum}')
# print(prefix_sum[7] - prefix_sum[0])
# print(prefix_sum[8] - prefix_sum[1])
# print(prefix_sum[9] - prefix_sum[2])
