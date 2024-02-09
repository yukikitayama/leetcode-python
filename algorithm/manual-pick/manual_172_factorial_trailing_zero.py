class Solution:
    def trailingZeroes(self, n: int) -> int:

        # Computer factorial
        fact = 1
        for i in range(1, n + 1):
            fact *= i

        print(fact)

        # Count zero
        ans = 0
        while fact % 10 == 0:
            ans += 1
            fact //= 10

        return ans


if __name__ == "__main__":
    n = 5
    n = 3
    n = 0
    n = 30
    print(Solution().trailingZeroes(n))
