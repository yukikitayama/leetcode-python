"""
for each number from 1 to n
  compute sum of digits
  save to hashmap k: sum, v: list of numbers
  save max length of list
iterate hashmap
  if list length is max length
    increment answer counter
"""

import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digit(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        sum_to_nums = collections.Counter()
        max_length = 0
        for num in range(1, n + 1):
            sum_ = sum_digit(num)
            sum_to_nums[sum_] += 1
            max_length = max(max_length, sum_to_nums[sum_])
        ans = 0
        for k, v in sum_to_nums.items():
            if v == max_length:
                ans += 1
        return ans

    def countLargestGroup1(self, n: int) -> int:

        def sum_digit(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        sum_to_nums = collections.defaultdict(list)
        max_length = 0
        for num in range(1, n + 1):
            sum_ = sum_digit(num)
            sum_to_nums[sum_].append(num)
            max_length = max(max_length, len(sum_to_nums[sum_]))

        # print(max_length)
        # print(sum_to_nums)

        ans = 0
        for k, v in sum_to_nums.items():
            if len(v) == max_length:
                ans += 1
        return ans


