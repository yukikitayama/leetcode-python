from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        pow2 = [1]
        for i in range(1, n):
            pow2.append(pow2[-1] * 2 % MOD)

        # print(f'pow2: {pow2}')

        ans = 0
        for i, x in enumerate(nums):
            ans = (ans + (pow2[i] - pow2[n - 1 - i]) * x) % MOD

        return ans


if __name__ == '__main__':
    print(Solution().sumSubseqWidths([2, 1, 3]))
