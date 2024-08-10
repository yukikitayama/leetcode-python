from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        subarray_sums = []
        curr_sum = 0
        for i, x in enumerate(nums):

            # Keep growing
            curr_sum += x

            if i >= k:
                # Keep the sum within k length interval
                curr_sum -= nums[i - k]

            if i >= k - 1:
                # Collect each subarray sum
                subarray_sums.append(curr_sum)

        # left contains index with max value so far from left
        left = [0] * len(subarray_sums)
        idx_max_so_far = 0
        for i in range(len(subarray_sums)):
            if subarray_sums[i] > subarray_sums[idx_max_so_far]:
                idx_max_so_far = i
            left[i] = idx_max_so_far

        right = [0] * len(subarray_sums)
        idx_max_so_far = len(subarray_sums) - 1
        for i in range(len(subarray_sums) - 1, -1, -1):
            # Why include =?
            if subarray_sums[i] >= subarray_sums[idx_max_so_far]:
                idx_max_so_far = i
            right[i] = idx_max_so_far

        # print(subarray_sums)
        # print(left)
        # print(right)

        ans = None
        for mid_idx in range(k, len(subarray_sums) - k):

            left_idx = left[mid_idx - k]
            right_idx = right[mid_idx + k]

            if ans is None or (
                    subarray_sums[left_idx] + subarray_sums[mid_idx] + subarray_sums[right_idx] > subarray_sums[
                ans[0]] + subarray_sums[ans[1]] + subarray_sums[ans[2]]):
                ans = [left_idx, mid_idx, right_idx]

        return ans