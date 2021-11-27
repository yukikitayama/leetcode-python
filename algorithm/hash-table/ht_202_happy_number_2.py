"""
- Floyd's cycle finding algorithm
"""


class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit**2
            return total_sum

        slow = n
        fast = get_next(n)
        while fast != 1 and fast != slow:
            fast = get_next(get_next(fast))
            slow = get_next(slow)
        return fast == 1


print(Solution().isHappy(7))
print(Solution().isHappy(116))

# num = 123
# while num > 0:
#     num, digit = divmod(num, 10)
#     print(f'num: {num}, digit: {digit}')


