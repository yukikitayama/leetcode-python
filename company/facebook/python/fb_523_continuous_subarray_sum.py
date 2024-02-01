"""
- Make all the prefix sums and find multiple

- If mod repeats, it means between two same mods, the sum was multiple of k
"""


from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum_to_index = {0: -1}
        sum_ = 0

        for i, num in enumerate(nums):

            sum_ += num
            if k != 0:
                sum_ %= k

            if sum_ not in prefix_sum_to_index:
                prefix_sum_to_index[sum_] = i

            else:
                if i - prefix_sum_to_index[sum_] > 1:

                    print(f'i: {i}, sum_: {sum_}')

                    return True

        print(prefix_sum_to_index)

        return False


if __name__ == '__main__':
    nums = [23,2,4,6,7]
    k = 6
    nums = [23, 2, 4, 6, 6]
    k = 7
    # true, 23 + 2 + 4 + 6 = 35, 7 * 5 = 35
    nums = [0]
    k = 1
    # false,
    nums = [1, 0]
    k = 2
    print(Solution().checkSubarraySum(nums, k))
