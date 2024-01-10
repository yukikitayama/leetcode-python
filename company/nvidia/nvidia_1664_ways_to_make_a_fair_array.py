"""
brute force
for each index removal, iterate removed array and compute even sum and odd sum, and check fairness

one pass
when element is removed at i, all the element after i change its odd/even. Even becomes odd, and odd becomes even
e.g. [1, 2, 3, 4], when we remove 2, [1, 3, 4], odd 3 becomes even, even 4 becomes odd
"""

from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        ans = 0

        for i in range(len(nums)):

            curr = nums[:]
            curr.pop(i)

            even_sum = 0
            odd_sum = 0

            for j in range(len(curr)):

                if j % 2 == 0:
                    even_sum += curr[j]
                else:
                    odd_sum += curr[j]

            if even_sum == odd_sum:
                ans += 1

        return ans

    def waysToMakeFair(self, nums: List[int]) -> int:
        ans = 0

        even_sum = sum(nums[::2])
        odd_sum = sum(nums[1::2])

        prev = 0

        for i in range(len(nums)):

            # Odd
            if i % 2 != 0:
                odd_sum += (-nums[i] + prev)

                if even_sum == odd_sum:
                    ans += 1

                prev = nums[i]

            # Even
            else:
                even_sum += (-nums[i] + prev)

                if even_sum == odd_sum:
                    ans += 1

                prev = nums[i]

        return ans


if __name__ == "__main__":
    nums = [2, 1, 6, 4]  # 1
    nums = [1, 1, 1]  # 3
    nums = [1, 2, 3]  # 0
    print(Solution().waysToMakeFair(nums))


