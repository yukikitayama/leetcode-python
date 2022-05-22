"""
- Reuse the previously calculated results
- Each state tells whether a unique string is a palindrome or not,
  counting True states provides us the number of palindromic substrings?
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        # print(f'dp: {dp}')

        ans = 0

        # Base case: single letter
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # Base case: 2 letters
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1

        # DP to check substring length more than 2
        for len_ in range(3, n + 1):

            # print(f'length: {len_}')

            # +1 because end index is exclusive
            # e.g. n: 4, len_: 3, range: (0, 1)
            for start in range(n - len_ + 1):

                # -1 because end needs to be inclusive for s[end]
                end = start + len_ - 1

                # print(f'  start: {start}, end: {end}')

                # Palindrome if inside is palindrome and current positions are the same character
                if dp[start + 1][end - 1] and s[start] == s[end]:
                    dp[start][end] = True
                    ans += 1

        return ans


class Solution1:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        for start in range(len(s)):
            for end in range(start, len(s)):

                if is_palindrome(start, end):
                    ans += 1

        return ans


if __name__ == '__main__':
    # s = "abc"
    # 3
    s = "aaa"
    # 6
    print(Solution().countSubstrings(s))
