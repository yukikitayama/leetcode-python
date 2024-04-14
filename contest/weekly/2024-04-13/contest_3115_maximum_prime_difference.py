"""
Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.
"""

from typing import List
import math


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def is_prime(n):

            if n <= 1:
                return False

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False

            return True

        left = None
        ans = 0
        primes = set()

        for i in range(len(nums)):

            num = nums[i]

            if num in primes:
                ans = max(ans, i - left)

            elif is_prime(num) and left is None:
                left = i
                primes.add(num)

            elif is_prime(num):
                primes.add(num)
                ans = max(ans, i - left)

        return ans
