"""
- Math?
- Bit mask?
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        # 26 because English has 26 letters
        freq = [0] * 26

        for i in range(len(s)):
            c = s[i]
            freq[ord(c) - ord('a')] += 1

        # print(f'freq: {freq}')

        ans = 0
        seen = set()

        for i in range(len(freq)):

            while freq[i] and freq[i] in seen:
                freq[i] -= 1
                ans += 1

            seen.add(freq[i])

        return ans


if __name__ == '__main__':
    s = "aab"
    # 0
    s = "aaabbbcc"
    # 2
    s = "ceabaacb"
    # 2
    print(Solution().minDeletions(s))
