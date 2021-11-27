"""
n: 7
7^2: 49
4^2 + 9^2: 16 + 81 = 97
9^2 + 7^2: 81 + 49 = 130
1^2 + 3^2 + 0^2: 1 + 9 = 10
1^2 + 0^2: 1
True

n: 116
1^2 + 1^2 + 6^2: 1 + 1 + 36 = 38
3^2 + 8^2: 9 + 64 = 73
7^2 + 3^2: 49 + 9 = 58
5^2 + 8^2: 25 + 64 = 89
...
3^2 + 7^2: 9 + 49 = 58,
cycle
False
"""


class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit**2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


print(Solution().isHappy(7))
print(Solution().isHappy(116))

# num = 123
# while num > 0:
#     num, digit = divmod(num, 10)
#     print(f'num: {num}, digit: {digit}')


