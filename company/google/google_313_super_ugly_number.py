from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        curr_ugly = 1
        dp = [curr_ugly]

        indices = [0] * len(primes)
        ugly_nums = [1] * len(primes)

        # Start with 1 because we 1st ugly number is always 1
        # so skip it. We can skip it because dp is initialized with dp: [1]
        for i in range(1, n):
            for j in range(0, len(primes)):
                if ugly_nums[j] == curr_ugly:
                    # ?
                    ugly_nums[j] = dp[indices[j]] * primes[j]
                    # We just used a prime at j, so increment it
                    indices[j] += 1

            # print(f'i: {i}, ugly_nums: {ugly_nums}, indices: {indices}')

            curr_ugly = min(ugly_nums)
            dp.append(curr_ugly)

            # print(f'  curr_ugly: {curr_ugly}, dp: {dp}')

        return dp[-1]


if __name__ == '__main__':
    n = 12
    primes = [2, 7, 13, 19]
    print(Solution().nthSuperUglyNumber(n, primes))
