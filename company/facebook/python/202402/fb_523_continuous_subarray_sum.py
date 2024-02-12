"""
Iterate
  Compute current prefix sum
  Compute the difference current prefix sum and previous prefix sum
    Both prefix sums share the same remainder
"""


from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder_to_index = {0: 0}

        curr_sum = 0

        for i in range(len(nums)):

            curr_sum += nums[i]

            remainder = curr_sum % k

            # print(curr_sum, remainder, i, remainder_to_index)

            if remainder not in remainder_to_index:
                # +1 to have at least two element
                remainder_to_index[remainder] = i + 1

            elif remainder_to_index[remainder] < i:
                return True

            # print("  ", curr_sum, remainder, i, remainder_to_index)

        return False


if __name__ == "__main__":
    nums = [23, 2, 4, 6, 7]
    k = 6
    # T, 2 + 4 = 6, multiple of 6

    # nums = [23, 2, 6, 4, 7]
    # k = 6
    # T, 23 + 2 + 6 + 4 + 7 = 42, multiple of 6, 6 * 7 = 42

    # nums = [23, 2, 6, 4, 7]
    # k = 13
    # F

    nums = [1, 10, 10, 17]
    k = 10
    # T, 10 + 10 + 20, multiple of 10, 10 * 2 = 20

    print(f"nums: {nums}, k: {k}")
    print(Solution().checkSubarraySum(nums, k))
