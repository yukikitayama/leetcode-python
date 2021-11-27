class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]

        for m in range(2, n + 1):

            i = 1
            j = m - i
            max_product = 0

            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                i += 1
                j -= 1

            dp.append(max_product)

        return dp[n]


print(Solution().integerBreak(2))
print(Solution().integerBreak(10))

