from typing import List
import collections
import math


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # Prepare divisor
        counter = collections.Counter([num2 * k for num2 in nums2])

        # Array to count the number of occurrence of divisors in the value range of nums1
        counts = [0] * (max(nums1) + 1)

        # Count the number of possible divisors
        for k, v in counter.items():
            # Step by k because that's also divisible
            for multiplier in range(k, len(counts), k):
                # Increment the occurrence by the number of appearance
                counts[multiplier] += v

        # To find pair, only extract the occurrence that num1 appears
        return sum(counts[num1] for num1 in nums1)

    def numberOfPairs1(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # Get all the factors for each number in nums1
        counter = collections.Counter()

        for num1 in nums1:

            for i in range(1, int(math.sqrt(num1)) + 1):

                q, r = divmod(num1, i)

                if r == 0:

                    if i * i == num1:
                        counter[i] += 1

                    else:
                        counter[i] += 1
                        counter[q] += 1

        # print(counter)

        ans = 0

        for num2 in nums2:

            if num2 * k in counter:
                ans += counter[num2 * k]

        return ans
