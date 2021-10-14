"""
A: 1, Z: 26

s: "12"
1, 2
12

s: "226"
2, 2, 6
2, 26
22, 6

s: "11106"
Good: 1, 1, 10, 6
Good: 11, 10, 6
Bad: 1, 1, 1, 06

- Brute force
- Initialize ans to 0
- Iterate start index
- Iterate end index
- Slice s by start index and end index
- If sliced number is valid, go to the next start and end index
- When end index reached the size of s, count up the number of ways to decode

- Top down dynamic programming
- The above uses recursion, so we can make a memoization table

- Bottom up dynamic programming
- dp[i] represents the number of ways with s[:i]
"""


from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def recursiveWithMemo(index, s) -> int:

            # If you reach the end of the string the digit was successfully decodable
            if index == len(s):
                return 1

            # If the string starts with a zero, there's no way to decode so 0 number of decodes
            if s[index] == '0':
                return 0

            # If the current index is the last digit, and it's not 0, it's decodable to A to some alphabet
            if index == len(s) - 1:
                return 1

            # Go to the next digit in s
            answer = recursiveWithMemo(index + 1, s)

            # +2 because end slicer is exclusive
            if int(s[index:index + 2]) <= 26:
                answer += recursiveWithMemo(index + 2, s)

            return answer

        return recursiveWithMemo(0, s)


s = "12"
s = "2326"
print(Solution().numDecodings(s))
