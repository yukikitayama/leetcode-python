class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        m = 0

        for num in s:
            if num == '0':
               m += 1

        ans = m

        for num in s:
            if num == '0':
                m -= 1
                ans = min(ans, m)
            elif num == '1':
                m += 1

        return ans


