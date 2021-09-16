

class Solution:
    def __init__(self):
        self.M = 10**9 + 7

    def checkRecord(self, n: int) -> int:
        f = [0] * (6 if n <= 5 else n + 1)
        f[0] = 1
        f[1] = 2
        f[2] = 4
        f[3] = 7

        for i in range(4, n + 1):
            f[i] = ((2 * f[i - 1]) % self.M + (self.M - f[i - 4])) % self.M

        summed = f[n]

        for i in range(1, n + 1):
            summed += (f[i - 1] * f[n - i]) % self.M

        return summed % self.M


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
