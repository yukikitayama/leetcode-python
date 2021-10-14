class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        source_len = len(s)
        target_len = len(t)

        if source_len == 0:
            return True

        dp = [[0] * (target_len + 1) for _ in range(source_len + 1)]

        for col in range(1, target_len + 1):
            for row in range(1, source_len + 1):
                # -1 because s is one length shorter than dp matrix
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

            # We wanna know whether s is subsequence of t
            # so once we find s is subsequence, we can finish
            # Thus we first exhaust all the char in s, that's why
            # row (source) is inner for loop.
            # source_len is the last index of s
            # col is the current index of target
            # dp[source_len][col] means exhausting all the s chars and current col
            # as long as it's source_len, it means all the characters in s were found in target
            # so return True
            if dp[source_len][col] == source_len:

                # print(f'  dp:')
                # [print(f'  {row}') for row in dp]

                return True

        print(f'dp:')
        [print(row) for row in dp]

        # Otherwise some characters in s were not found in target,
        # So return false
        return False


s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
s = 'abc'
t = 'abcde'
print(Solution().isSubsequence(s, t))

