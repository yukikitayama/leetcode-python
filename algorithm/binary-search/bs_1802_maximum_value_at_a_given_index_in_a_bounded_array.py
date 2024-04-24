"""
Sum of arithmetic sequence
  (a1 + an) * (n / 2)

Left
  when value <= index
    value: 3, index: 6
    [1, 1, 1, 1, 1, 2, 3]
    index - value + 1 = 6 - 3 + 1 = 4
      length and sum of continous sequence of 1s
    value
      length of arithmetic sequence from value to 1
      (1 + (value)) * (value / 2) is the sum of the arithmetic sequence
  when value > index
    value: 5, index: 3
    [2, 3, 4, 5]
    a1: value - index = 2, an: value = 5, so sum is (value - index + value) * ((index + 1) / 2)

Right
  n: length of array
  value <= n - index
    value: 5, n: 9, index: 0
    [5, 4, 3, 2, 1, 1, 1, 1, 1]
    arithmetic seq len: 5
    1s len: 4
  value > n - index
    value: 5, n: 4, index: 0
    [5, 4, 3, 2]
    arith lem: 4,
    1s len: 0
"""


class Solution:
    # def maxValue(self, n: int, index: int, maxSum: int) -> int:

    #     def get_sum(mid):
    #         sum_ = 0

    #         # Left
    #         if mid > index:
    #             sum_ += (mid - index + mid) * ((index + 1) // 2)
    #         else:
    #             # (arithmetic sequence) + (1s)
    #             sum_ += (1 + mid) * (mid // 2) + (index - mid + 1)

    #         # Right
    #         if mid >= n - index:
    #             sum_ += (mid + mid - n + 1 + index) * (n - index) // 2
    #         else:
    #             # (arithmetic sequence) + (1s)
    #             sum_ += (1 + mid) * (mid // 2) + (n - index - mid)

    #         # value was double-counted
    #         return sum_ - mid

    #     # Binary search
    #     left = 1
    #     right = maxSum
    #     while left < right:
    #         mid = (left + right + 1) // 2

    #         res = get_sum(mid)

    #         if res <= maxSum:
    #             left = mid
    #         else:
    #             right = mid - 1

    #     print(left, right)

    #     return left

    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0

        # On index's left:
        # If value > index, there are index + 1 numbers in the arithmetic sequence:
        # [value - index, ..., value - 1, value].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [1, 2, ..., value - 1, value], plus a sequence of length (index - value + 1) of 1s.
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1

        # On index's right:
        # If value >= n - index, there are n - index numbers in the arithmetic sequence:
        # [value, value - 1, ..., value - n + 1 + index].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [value, value - 1, ..., 1], plus a sequence of length (n - index - value) of 1s.
        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value

        return count - value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left
