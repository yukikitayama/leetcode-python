"""
i, j, k act like walls
  split array into 4 subarrays
"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        """T: O(N**2), S: O(N)"""
        n = len(nums)

        # nums: [1, |, 1, |, 1, |]
        if n < 7:
            return False

        # Prefix sum
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        # For each mid cut j
        for j in range(3, n - 3):

            sum_set = set()

            # Check left side of j
            for i in range(1, j - 1):

                if prefix_sum[i - 1] == (prefix_sum[j - 1] - prefix_sum[i]):
                    sum_set.add(prefix_sum[i - 1])

            # Check right side of j
            for k in range(j + 2, n - 1):

                if (prefix_sum[k - 1] - prefix_sum[j]) == (prefix_sum[n - 1] - prefix_sum[k]):
                    if (prefix_sum[k - 1] - prefix_sum[j]) in sum_set:
                        return True

        return False

    def splitArray2(self, nums: List[int]) -> bool:
        n = len(nums)

        # nums: [1, |, 1, |, 1, |]
        if n < 7:
            return False

        # Prefix sum
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        # print(prefix_sum)

        # i: 1 <= i <= n - 6
        # j: 3 <= j <= n - 4
        # k: 5 <= k <= n - 2
        for i in range(1, n - 5):

            sum1 = prefix_sum[i - 1]

            for j in range(i + 2, n - 3):

                sum2 = prefix_sum[j - 1] - prefix_sum[i]

                # Little improvement
                if sum1 != sum2:
                    continue

                for k in range(j + 2, n - 1):

                    sum3 = prefix_sum[k - 1] - prefix_sum[j]
                    sum4 = prefix_sum[n - 1] - prefix_sum[k]

                    if sum1 == sum2 and sum2 == sum3 and sum3 == sum4:
                        return True

        return False

    def splitArray1(self, nums: List[int]) -> bool:

        n = len(nums)

        # nums: [1, |, 1, |, 1, |]
        if n < 7:
            return False

        # i: 1 <= i <= n - 6
        # j: 3 <= j <= n - 4
        # k: 5 <= k <= n - 2
        for i in range(1, n - 5):

            sum1 = sum(nums[0:i])

            for j in range(i + 2, n - 3):

                sum2 = sum(nums[i + 1:j])

                for k in range(j + 2, n - 1):

                    sum3 = sum(nums[j + 1:k])
                    sum4 = sum(nums[k + 1:])

                    if sum1 == sum2 and sum2 == sum3 and sum3 == sum4:
                        return True

        return False