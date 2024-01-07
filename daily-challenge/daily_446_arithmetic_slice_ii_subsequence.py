"""
- backtracking but brute force

"""

from typing import List
import collections


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        ans = 0

        cnt = collections.defaultdict(collections.defaultdict)

        for i in range(len(nums)):

            cnt[i] = collections.defaultdict(int)

            for j in range(i):

                diff = nums[i] - nums[j]

                sum_ = cnt[j][diff]

                origin = cnt[i][diff]

                cnt[i][diff] = origin + sum_ + 1

                ans += sum_

        return ans


if __name__ == "__main__":
    nums = [2, 4, 6, 8, 10]
    nums = [7, 7, 7, 7, 7]
    print(Solution().numberOfArithmeticSlices(nums))


