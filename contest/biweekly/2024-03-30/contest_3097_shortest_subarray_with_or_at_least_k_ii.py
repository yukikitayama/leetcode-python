"""
Sliding window
nums: [1, 2, 3], k: 2
bins: [01, 10, 11]
prefix OR: [01, 11, 11]
bin: 11 = 3 >= k: 2

Hashmap
  k: bitwise position
  v: count of 1

{0: 1}, {0: 1, 1: 1}, {0: 2, 1: 2}
"""

from typing import List
import collections


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def convert(num):

            bined = bin(num)
            bits = bined[2:]

            counter = collections.Counter()

            for i in range(len(bits)):
                if bits[-(i + 1)] == "1":
                    counter[i] = 1

            return counter

        def deconvert(counter):
            ans = 0
            for k, v in counter.items():
                if v > 0:
                    ans += 2 ** k
            return ans

        ans = float("inf")

        left = 0
        bit_to_count = collections.Counter()

        for right in range(len(nums)):
            num = nums[right]
            curr_counter = convert(num)

            bit_to_count += curr_counter
            de_num = deconvert(bit_to_count)

            # print(f"num: {num}, curr_counter: {curr_counter}, bit_to_count: {bit_to_count}, de_num: {de_num}")

            while left <= right and de_num >= k:
                ans = min(ans, right - left + 1)
                num_left = nums[left]
                left_counter = convert(num_left)
                bit_to_count -= left_counter
                de_num = deconvert(bit_to_count)

                left += 1

        # print()

        return -1 if ans == float("inf") else ans

    def minimumSubarrayLength1(self, nums: List[int], k: int) -> int:

        ans = float("inf")

        for start in range(len(nums)):
            prefix_or = 0
            for end in range(start, len(nums)):
                prefix_or |= nums[end]

                if prefix_or >= k:
                    ans = min(ans, end - start + 1)

        return -1 if ans == float("inf") else ans

