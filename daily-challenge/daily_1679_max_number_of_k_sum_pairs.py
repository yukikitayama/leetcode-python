"""
- Dictionary
- Find complement y = k - x
"""


from typing import List
import collections


# One pass
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = collections.Counter()

        for i in range(len(nums)):

            # print(f'i: {i}')

            curr = nums[i]
            complement = k - curr

            if counter[complement] > 0:

                counter[complement] -= 1
                ans += 1

            else:
                counter[curr] += 1

            # print(f'  counter: {counter}')

        return ans


# Two pass
class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        ans = 0
        for i in range(len(nums)):
            curr = nums[i]
            complement = k - curr

            if counter[curr] > 0 and counter[complement] > 0:

                if curr == complement and counter[curr] < 2:
                    continue

                counter[curr] -= 1
                counter[complement] -= 1

                ans += 1

            # print(f'counter: {counter}')

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    k = 5
    nums = [3, 1, 3, 4, 3]
    k = 6
    # 1
    print(Solution().maxOperations(nums, k))
