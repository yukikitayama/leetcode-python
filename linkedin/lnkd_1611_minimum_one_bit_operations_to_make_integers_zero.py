class Solution:
    def __init__(self):
        self.dp = {0: 0}

    def minimumOneBitOperations(self, n: int) -> int:
        if n not in self.dp:
            b = 1
            while (b << 1) <= n:
                b = b << 1

            print(f'  b: {b}, bin(b): {bin(b)}')

            print(f'    b >> 1: {bin(b >> 1)}, b: {bin(b)}, (b >> 1) ^ b: {bin((b >> 1) ^ b)}, '
                  f'n: {bin(n)}, (b >> 1) ^ b ^ n: {bin((b >> 1) ^ b ^ n)}, '
                  f'')

            self.dp[n] = self.minimumOneBitOperations((b >> 1) ^ b ^ n) + 1 + b - 1

        print(f'  return self.dp[{n}], {self.dp[n]}')

        return self.dp[n]


print(Solution().minimumOneBitOperations(0))
print(Solution().minimumOneBitOperations(3))
print(Solution().minimumOneBitOperations(4))



