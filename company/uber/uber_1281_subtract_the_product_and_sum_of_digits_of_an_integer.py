class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_ = 0

        # This gets digit from left
        # for digit in str(n):
        #     product *= int(digit)
        #     sum_ += int(digit)

        # This gets digits from right
        while n:
            # n: 123, divmod(n, 10): divmod(123, 10), n: 12, digit: 3
            # divmod(12, 10), n: 1, digit: 2
            # divmod(1, 10), n: 0, digit: 1
            n, digit = divmod(n, 10)
            sum_ += digit
            product *= digit

        return product - sum_


"""
Complexity
- Time is O(logn) with n is the given n, where base of log is 10
- Space is O(1)

- The number of digits is log(N), where N is the number n
  - Base of log is 10
    - log_10 10 = 1,
    - log_10 100 = log_10 10^2 = 2
    - log_10 1000 = log_10 10^3 = 3
  - each digit represents {digit}*10^(k-th location)
"""


n = 234  # 15
n = 4421  # 21
print(Solution().subtractProductAndSum(n))
