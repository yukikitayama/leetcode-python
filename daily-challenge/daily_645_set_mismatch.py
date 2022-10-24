from typing import List
import collections


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        counter = collections.defaultdict(int)
        for i in range(1, n + 1):
            counter[i] = 0

        for num in nums:
            counter[num] += 1

        ans = [None, None]

        for k, v in counter.items():
            if v == 2:
                ans[0] = k
            elif v == 0:
                ans[1] = k

        return ans


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    print(Solution().findErrorNums(nums))
