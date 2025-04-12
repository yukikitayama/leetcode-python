class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        def is_symmetric(num):
            digits = str(num)
            if len(digits) % 2 != 0:
                return False

            sum_ = sum(int(d) for d in digits)

            left_sum = 0

            for i in range(len(digits) // 2):
                left_sum += int(digits[i])

            # print(f"num: {num}, sum_: {sum_}, left_sum: {left_sum}")

            return sum_ / 2 == left_sum

        ans = 0
        for num in range(low, high + 1):
            if is_symmetric(num):
                ans += 1
        return ans