from typing import List
import collections


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        def rev(num):

            reversed_num = 0

            while num != 0:

                last_digit = num % 10
                num //= 10

                reversed_num *= 10
                reversed_num += last_digit

            return reversed_num

        diffs = []
        for num in nums:
            diffs.append(num - rev(num))

        diff_to_count = collections.defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7

        for diff in diffs:

            ans = (ans + diff_to_count[diff]) % MOD

            diff_to_count[diff] += 1

        return ans


if __name__ == "__main__":
    nums = [42, 11, 1, 97]
    nums = [13, 10, 35, 24, 76]
    print(Solution().countNicePair(nums))
