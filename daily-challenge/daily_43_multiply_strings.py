"""
- 1 2 3
* 4 5 6
  - 123 * 6 = 738
  - 123 * 5 = 615
  - 123 * 4 = 492
= 56088
  - 738 + 6150 + 49200

- carry
- answer from the first digit
- answer from the second digit
  -

- Time is O(n^2)
- Space is O(1)
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiplied = 0

        digit_2 = 1
        for j in range(len(num2) - 1, -1, -1):

            num = num2[j]

            ans = 0
            digit = 1
            for i in range(len(num1) - 1, -1, -1):
                value = (int(num) * int(num1[i])) % 10
                carry = (int(num) * int(num1[i])) // 10

                ans += value * digit
                digit *= 10
                ans += carry * digit

            # print(f'ans: {ans}, ans * digit_2: {ans * digit_2}')
            multiplied += digit_2 * ans

            # print(f'multiplied: {multiplied}')

            digit_2 *= 10

        return str(multiplied)


num1 = "123"
num2 = "456"
print(Solution().multiply(num1, num2))
