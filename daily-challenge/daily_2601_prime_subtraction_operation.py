from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def is_prime(x):
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        for i in range(len(nums)):

            if i == 0:
                bound = nums[i]

            else:
                bound = nums[i] - nums[i - 1]

            if bound <= 0:
                return False

            largest_prime = 0
            for j in range(bound - 1, 1, -1):
                if is_prime(j):
                    largest_prime = j
                    break

            nums[i] = nums[i] - largest_prime

        return True