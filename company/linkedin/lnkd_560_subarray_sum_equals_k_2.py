"""
- The idea is based on prefix sum and the difference between prefix[j] and prefix[i]
  to get the sum between i and j
"""


from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0

        # Current prefix sum
        sum = 0

        # Hashmap with key prefix sum and value the count
        map = collections.defaultdict(int)
        map[0] = 1

        for i in range(len(nums)):
            sum += nums[i]

            print(f'i: {i}, nums[i]: {nums[i]}, sum: {sum}, map: {map}')

            # this does prefix[j] - prefix[i] to get sum between i and j
            if sum - k in map:

                print(f'  sum - k: {sum - k}, map[sum - k]: {map[sum - k]}')

                ans += map[sum - k]

            map[sum] += 1

        return ans


# nums = [1,1,1]
# k = 2
nums = [1,2,3]
k = 3
nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(Solution().subarraySum(nums, k))



