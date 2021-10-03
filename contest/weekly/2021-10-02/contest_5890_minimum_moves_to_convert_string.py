class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        ans = 0
        while i < len(s):
            if s[i] == 'X':
                i += 3
                ans += 1
            else:
                i += 1

        return ans


s = 'XXX'
s = "XXOX"
# s = "OOOO"
# s = "OXOX"
print(Solution().minimumMoves(s))
