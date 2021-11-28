

class Solution:
    def __init__(self):
        self.M = 10**9 + 7

    def checkRecord(self, n: int) -> int:
        f = [0] * (n + 1)
        f[0] = 1

        for i in range(1, n + 1):
            f[i] = self.func(i)

        # print(f'f after 1st for loop: {f}')

        summed = self.func(n)

        # print(f'summed before for loop: {summed}')

        for i in range(1, n + 1):
            summed += (f[i - 1] * f[n - i]) % self.M

            # print(f'f[i - 1]: {f[i - 1]}, f[n - i]: {f[n - i]}')

        # print(f'summed after for loop: {summed}')

        return summed % self.M

    def func(self, n: int):
        if n == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 4
        if n == 3:
            return 7
        return (2 * self.func(n - 1) - self.func(n - 4)) % self.M



"""
Answers
n: 2, output: 8
n: 3, output: 19
n: 4, output: 43
n: 10, output: 3536
"""



# print(Solution().checkRecord(2))
# print(Solution().checkRecord(1))
# print(Solution().checkRecord(10101))
# print(Solution().checkRecord(3))
print(Solution().checkRecord(4))
