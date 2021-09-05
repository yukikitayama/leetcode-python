class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        # print(f'x: {x}, result: {result}')
        while x:
            result = result * 10 + x % 10
            x //= 10
            # print(f'x: {x}, result: {result}')

        return 0 if result > pow(2, 31) else result * symbol


x = 123
x = -123
print(Solution().reverse(x))
