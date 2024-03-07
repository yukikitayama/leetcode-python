from typing import List
import collections


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = sum(nums[:k])
        curr_set = collections.Counter(nums[:k])
        ans = 0
        if len(curr_set.keys()) == k:
            ans = max(ans, curr_sum)

        # 3, 7 - 3 = 4
        for i in range(k, len(nums)):
            curr_sum -= nums[i - k]
            curr_set[nums[i - k]] -= 1
            if curr_set[nums[i - k]] == 0:
                del curr_set[nums[i - k]]

            curr_sum += nums[i]
            curr_set[nums[i]] += 1

            # print(i, nums[i], curr_sum, curr_set)

            if len(curr_set.keys()) == k:
                ans = max(ans, curr_sum)

        return ans