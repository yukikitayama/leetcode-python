import functools


class Solution:
    def numDecodings(self, s: str) -> int:

        @functools.lru_cache(maxsize=None)
        def recursion(i):

            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            # If currently at the last character in s and we already checked it's not 0
            # so the current character is from 1 to 9, which is valid
            if i == len(s) - 1:
                return 1

            ans = recursion(i + 1)

            if int(s[i:i + 2]) <= 26:
                ans += recursion(i + 2)

            return ans

        return recursion(0)


if __name__ == '__main__':
    s = "226"
    print(Solution().numDecodings(s))
