from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = []

        def backtrack(result, s, start, curr, dp):
            if start >= len(s):
                result.append(curr[:])

            for end in range(start, len(s)):
                # end - start <= 2, e.g. end: 2, start: 0, one character in middle
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    curr.append(s[start:end + 1])
                    # end + 1 because end is inclusive, and next string start should be end + 1
                    backtrack(result, s, end + 1, curr, dp)
                    # Backtrack
                    curr.pop()

        backtrack(result, s, 0, [], dp)

        return result


if __name__ == '__main__':
    s = 'aab'
    print(Solution().partition(s))