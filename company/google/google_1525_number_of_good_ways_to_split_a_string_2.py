import collections


class Solution:
    def numSplits(self, s: str) -> int:
        left = collections.Counter()
        right = collections.Counter(s)

        ans = 0

        for char in s:

            left[char] += 1
            right[char] -= 1

            if right[char] == 0:
                del right[char]

            if len(left) == len(right):
                ans += 1

        return ans


s = "aacaba"
s = "acbadbaada"
print(Solution().numSplits(s))
