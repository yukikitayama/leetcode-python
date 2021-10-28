"""
- log multiple of xs = sum of log xs
"""


from typing import List
import math
import bisect


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Constraints says all the num in nums are bigger than 0
        if k == 0:
            return 0

        k = math.log(k)

        prefix = [0]
        for num in nums:

            print(f'num: {num}, math.log(num): {math.log(num)}')

            prefix.append(prefix[-1] + math.log(num))

        print(f'k: {k}, prefix: {prefix}')

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i + 1)
            ans += j - i - 1

        return ans


nums = [10,5,2,6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))

