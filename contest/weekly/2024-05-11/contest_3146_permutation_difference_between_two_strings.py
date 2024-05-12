class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_to_i = {s[i]: i for i in range(len(s))}

        ans = 0

        for i in range(len(t)):
            ans += abs(s_to_i[t[i]] - i)

        return ans
