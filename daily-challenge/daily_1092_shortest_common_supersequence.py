"""
brute force

Supersequence
A supersequence of a string is a sequence that includes the original string as a subsequence. This means we can derive the original string by removing certain characters without altering the relative order of the remaining ones.

The Shortest Common Supersequence (SCS) is the smallest string that contains both str1 and str2 as subsequences.

This problem is closely linked to the Longest Common Subsequence (LCS).

To form the SCS, we preserve the LCS while inserting the remaining characters from both strings around it, ensuring that the final sequence maintains the relative order of all characters.

dp[row - 1][col] represents including a character from str1 and dp[row][col - 1] represents including a character from str2.
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        str1_length = len(str1)
        str2_length = len(str2)

        dp = [
            [0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)
        ]

        for row in range(str1_length + 1):
            dp[row][0] = row

        for col in range(str2_length + 1):
            dp[0][col] = col

        for row in range(1, str1_length + 1):
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

        super_sequence = []
        row = str1_length
        col = str2_length
        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
            elif dp[row - 1][col] >= dp[row][col - 1]:
                super_sequence.append(str2[col - 1])
                col -= 1
        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1
        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1

        return "".join(super_sequence[::-1])

    def shortestCommonSupersequence3(self, str1: str, str2: str) -> str:

        str1_length = len(str1)
        str2_length = len(str2)

        prev_row = [str2[0:col] for col in range(str2_length + 1)]

        for row in range(1, str1_length + 1):

            curr_row = [str1[0:row]] + [None for _ in range(str2_length)]

            for col in range(1, str2_length + 1):

                if str1[row - 1] == str2[col - 1]:

                    curr_row[col] = prev_row[col - 1] + str1[row - 1]

                else:

                    pick_s1 = prev_row[col]
                    pick_s2 = curr_row[col - 1]

                    curr_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )

            prev_row = curr_row

        return prev_row[str2_length]

    def shortestCommonSupersequence2(self, str1: str, str2: str) -> str:

        memo = {}

        def recursion(s1, s2):
            memo_key = (s1, s2)

            if memo_key in memo:
                return memo[memo_key]

            if not s1 and not s2:
                return ""

            if not s1:
                return s2

            if not s2:
                return s1

            if s1[0] == s2[0]:
                memo[memo_key] = s1[0] + recursion(s1[1:], s2[1:])
                return memo[memo_key]

            pick_s1 = s1[0] + recursion(s1[1:], s2)
            pick_s2 = s2[0] + recursion(s1, s2[1:])

            memo[memo_key] = pick_s1 if len(pick_s1) < len(pick_s2) else pick_s2

            return memo[memo_key]

        return recursion(str1, str2)

    def shortestCommonSupersequence1(self, str1: str, str2: str) -> str:

        if not str1 and not str2:
            return ""

        if not str1:
            return str2

        if not str2:
            return str1

        if str1[0] == str2[0]:
            return str1[0] + self.shortestCommonSupersequence(str1[1:], str2[1:])

        else:
            pick_str1 = str1[0] + self.shortestCommonSupersequence(str1[1:], str2)
            pick_str2 = str2[0] + self.shortestCommonSupersequence(str1, str2[1:])

            return pick_str1 if len(pick_str1) < len(pick_str2) else pick_str2