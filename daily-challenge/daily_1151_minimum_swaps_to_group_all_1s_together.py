from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_ones = sum(data)
        max_so_far = 0
        curr_one = 0
        left = 0
        for right in range(len(data)):

            curr_one += data[right]

            if right - left + 1 > num_ones:
                curr_one -= data[left]
                left += 1

            max_so_far = max(max_so_far, curr_one)

        return num_ones - max_so_far

