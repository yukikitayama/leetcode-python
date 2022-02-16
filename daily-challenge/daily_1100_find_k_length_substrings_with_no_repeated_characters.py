class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ans = 0
        left = right = 0
        freq = [0] * 26

        while right < len(s):
            freq[ord(s[right]) - ord('a')] += 1

            # Contract
            while freq[ord(s[right]) - ord('a')] > 1:
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Check non duplicate k length
            if right - left + 1 == k:
                ans += 1

                # Contract
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Expand
            right += 1

        return ans


class Solution1:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ans = 0
        for i in range(k, len(s) + 1):
            substring = s[i - k:i]

            # print(f'substring: {substring}')

            if len(set(substring)) == k:
                ans += 1
        return ans


if __name__ == '__main__':
    s = "havefunonleetcode"
    k = 5
    print(Solution().numKLenSubstrNoRepeats(s, k))
