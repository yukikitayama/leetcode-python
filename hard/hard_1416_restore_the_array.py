import functools


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i]: number of arrays by using s[0:i]
        dp = [0] * (len(s) + 1)

        # Base case: There is one array (empty array) that can be printed as an empty string
        dp[0] = 1

        for start in range(len(s)):

            # 0 and leading 0 are not allowed
            if s[start] == "0":
                continue

            for end in range(start, len(s)):
                curr = s[start:end + 1]

                if int(curr) > k:
                    break

                dp[end + 1] += dp[start]
                dp[end + 1] %= MOD

        return dp[-1]

    def numberOfArrays1(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.cache
        def dp(index):

            # Base case
            if index == len(s):
                return 1

            # int("01") is 1, but it's not valid, so stop going to recurrence relation
            if s[index] == "0":
                return 0

            # Recurrence relation
            # +1 for slice exclusive
            ans = 0
            for i in range(index, len(s)):

                curr_num = int(s[index:i + 1])

                # If current number exceed k, pointless to increment i further to get a bigger number
                # So use the below break statement to finish for-loop earlier
                # The below 1 <= curr_num <= k approach will be TLE
                # if 1 <= curr_num <= k:
                #     ans += dp(i + 1)

                if curr_num > k:
                    break

                ans += dp(i + 1)
                ans %= MOD

            return ans

        return dp(0)