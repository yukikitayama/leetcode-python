"""
   [23, 2,  4,  6,  7]
[0, 23, 25, 29, 35, 42]

29 - 23 = 6
  i: 3 - i: 1
35 - 23 = 12
  i: 4 - i: 1

  T: O(N**2) not accepted


Ans
  Hashmap
    k: remainder of current prefix sum divided by k
    v: first index seen
  iterate
    prefix sum

"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_to_index = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            remainder = prefix_sum % k

            if remainder in remainder_to_index:
                prev = remainder_to_index[remainder]
                if i - prev > 1:
                    # print("True")
                    return True

            else:
                remainder_to_index[remainder] = i

            # print(prefix_sum, remainder_to_index)

        return False

    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        prefix_sums = [0]
        for i in range(len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])

        for right in range(2, len(prefix_sums)):
            for left in range(0, right - 2 + 1):
                diff = prefix_sums[right] - prefix_sums[left]
                if diff % k == 0:
                    # print(f"left: {left}, right: {right}, diff: {diff}")
                    return True

        return False

