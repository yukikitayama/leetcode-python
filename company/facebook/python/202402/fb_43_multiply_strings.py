"""
From right to left
  bitwise product
  product // 10 will be carry
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if len(num2) <= len(num1):
            base = num2
            top = num1
        else:
            base = num1
            top = num2

        ans = 0

        for b in range(len(base)):

            carry = 0
            num_b = int(base[-(b + 1)])
            curr_num = 0

            for t in range(len(top)):
                num_t = int(top[-(t + 1)])

                product = num_t * num_b + carry
                curr = product % 10
                carry = product // 10

                curr_num = curr_num + curr * (10**t)

            if carry:
                curr_num = curr_num + carry * (10**len(top))

            curr_num = curr_num * (10**b)
            ans += curr_num

        return str(ans)