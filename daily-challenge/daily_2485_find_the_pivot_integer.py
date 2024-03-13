"""
Compute right sum
Increment left sum
Compare
Decrement right sum

Formula
  n: 4, 1 + 2 + 3 + 4 = 10

n * (n + 1) / 2 - 4 * 5 / 2 = 20 / 2 = 10
"""


class Solution:
    def pivotInteger(self, n: int) -> int:

        # Edge case
        if n == 1:
            return 1

        left = 1
        right = n

        left_sum = 1
        right_sum = n

        while left < right:

            if left_sum < right_sum:
                left += 1
                left_sum += left

            # left_sum > right_sum
            else:
                right -= 1
                right_sum += right

            # When sum is equal and no middle number between left and right,
            # even length and no pivot
            if left_sum == right_sum and left + 1 == right - 1:
                return left + 1

        return -1

    def pivotInteger1(self, n: int) -> int:

        def get_total(n):
            ans = 0
            curr = 1

            while curr <= n:
                ans += curr
                curr += 1

            return ans

        right_sum = get_total(n)
        left_sum = 0

        # print(f"right_sum: {right_sum}")

        left = 1

        while left_sum <= right_sum:

            left_sum += left

            if left_sum == right_sum:
                return left

            else:
                right_sum -= left
                left += 1

        return -1
