from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            correct_idx = nums[i] - 1

            if 0 < nums[i] <= n and nums[correct_idx] != nums[i]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        n = len(nums)
        contains_1 = False

        for i in range(n):

            if nums[i] == 1:
                contains_1 = True

            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Edge case
        if not contains_1:
            return 1

        for i in range(n):
            # Alway positive to work as index
            num = abs(nums[i])

            # When num is n, there is not index n, because largest is n - 1
            # but we don't need num 0 too, so we use nums[0] to contain n
            if num == n:
                nums[0] = -abs(nums[0])

            else:
                # Mark current num exists
                nums[num] = -abs(nums[num])

        # Find missing smallest positive
        for i in range(1, n):
            # If positive, we didn't mark it exists, so missing
            if nums[i] > 0:
                return i

         # Above doesn't check n, because n is marked at special position of 0 index
        if nums[0] > 0:
            return n

        # Case where no missing integer in nums, but smallest missing is n + 1
        return n + 1

    def firstMissingPositive1(self, nums: List[int]) -> int:
        n = len(nums)

        # +1 because first element for 0, but we don't need 0
        seen = [False] * (n + 1)

        for num in nums:
            # num could be bigger than n, but we only care the first smallest positive integer
            if 0 < num <= n:
                seen[num] = True

        for i in range(1, n + 1):
            if not seen[i]:
                return i

        return n + 1