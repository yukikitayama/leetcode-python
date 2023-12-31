import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        str_to_idx = collections.defaultdict(int)

        ans = -1

        for i in range(len(s)):

            if s[i] not in str_to_idx:
                str_to_idx[s[i]] = i

            else:
                j = str_to_idx[s[i]]
                ans = max(ans, i - j - 1)

        return ans


if __name__ == "__main__":
    s = "aa"
    s = "abca"
    s = "cbzxy"
    print(Solution().maxLengthBetweenEqualCharacters(s))
