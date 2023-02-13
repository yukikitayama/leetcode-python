class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 0:
            low += 1

        return (high - low) // 2 + 1


if __name__ == "__main__":
    low = 3
    high = 7
    print(Solution().countOdds(low, high))
