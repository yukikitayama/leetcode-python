from typing import List
import collections


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_to_count = collections.defaultdict(int)
        prefix_sum_to_count[prefix_sum] += 1

        ans = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 1:
                prefix_sum += 1

            if prefix_sum - k in prefix_sum_to_count:
                ans += prefix_sum_to_count[prefix_sum - k]

            prefix_sum_to_count[prefix_sum] += 1

            # print(prefix_sum, prefix_sum_to_count)

        return ans

    def numberOfSubarrays1(self, nums: List[int], k: int) -> int:

        bin_nums = []
        for num in nums:
            if num % 2 == 0:
                bin_nums.append(0)
            else:
                bin_nums.append(1)

        print(bin_nums)

        return 0