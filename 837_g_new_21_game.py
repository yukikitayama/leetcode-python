class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        # print(f'n: {n}, k: {k}, maxPts: {maxPts}')

        # k == 0
        # When k is 0, Alice can draws while her score is less than k,
        # Her score: 0 < k: 0. This is False, so False from the beginning,
        # so the point stays at the initial 0.
        # Because n constraint is 0 <= n, so it's 100% that
        # point is equal to n (n: 0) or smaller than n.

        # n > k + maxPts
        # With k and maxPts, the maximum score that Alice can make is (k + maxPts - 1).
        # So as long as n is greater than (k + maxPts - 1), Alice's score is definitely less
        # than n, so probability to get less than n is 100%
        if k == 0 or n > k + maxPts - 1:
            return 1

        # ?
        # dp[i] is the probability that we get point i at some moment
        # e.g. dp[0] is the probability that we get point 0
        # dp[1] is the probability that we get point 1
        # 1 - dp[i] is the probability that we skip the point i
        # e.g. 1 - dp[2] is the probability that we don't get point 2
        # e.g. If dp[2] is 75%. We get 2 points with 75% probability and we don't get 2 points with 25%
        dp = [1.0] + [0.0] * n

        # ?
        Wsum = 1.0

        for i in range(1, n + 1):

            # print(f'i: {i}, Wsum: {Wsum}')

            # dp[i] is the probability to get i point
            # e.g. i: 1, Wsum: 1 and maxPts: 2, dp[1] is 1 / 2 = 0.5
            # It's correct because you get 1 point out of [1, 2] and get 2 points out of [1, 2]
            # e.g. i: 1, Wsum: 1 and maxPts: 10, dp[1] is 10%,
            # because get 1 out of [1, 2, 3, ..., 9, 10], so 10%
            dp[i] = Wsum / maxPts

            # If i is smaller than k
            if i < k:
                Wsum += dp[i]

            # ?
            if i - maxPts >= 0:
                Wsum -= dp[i - maxPts]

            print(f'i: {i}, dp[i]: {dp[i]}, Wsum: {Wsum}')

        # print(dp)

        # ?
        return sum(dp[k:])


n = 10
k = 1
maxPts = 10
# n = 6
# k = 1
# maxPts = 10
# n = 21
# k = 17
# maxPts = 10
n = 6
k = 2
maxPts = 10
print(Solution().new21Game(n, k, maxPts))

