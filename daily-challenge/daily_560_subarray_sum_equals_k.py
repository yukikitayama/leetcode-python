"""
- Current cumulative sum - k
  - Current cumulative sum - Previously happened cumulative sum = k
    - It says sum of nums between current index and previous index is k
"""


from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum_to_count = collections.defaultdict(int)
        sum_to_count[0] += 1
        cumsum = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            if cumsum - k in sum_to_count:
                ans += sum_to_count[cumsum - k]
            sum_to_count[cumsum] += 1
            # print(sum_to_count)
        return ans


class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum_ = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sum_[i] = sum_[i - 1] + nums[i - 1]

        print(f'sum_: {sum_}')

        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if sum_[end] - sum_[start] == k:
                    ans += 1

        return ans


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    # nums = [1, 2, 3]
    # k = 3
    print(Solution().subarraySum(nums, k))
