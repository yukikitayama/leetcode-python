import collections


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        MOD = 10**9 + 7
        a = 26
        n = len(s)

        nums = [ord(s[i]) - ord('a') for i in range(n)]

        # Us binary search to find the longest duplicate substring
        start = -1
        left, right = 1, n - 1
        while left <= right:
            L = left + (right - left) // 2
            start_of_duplicate = self.search(L, a, MOD, n, nums)

            if start_of_duplicate != -1:
                left = L + 1
                start = start_of_duplicate
            else:
                right = L - 1

        return s[start : start + left - 1]

    def search(self, L, a, MOD, n, nums):
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % MOD

        seen = collections.defaultdict(list)
        seen[h].append(0)

        aL = pow(a, L, MOD)
        for start in range(1, n - L + 1):
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % MOD

            if h in seen:
                current_substring = nums[start : start + L]
                if any(current_substring == nums[index : index + L] for index in seen[h]):
                    return start

            seen[h].append(start)

        return - 1


s = "banana"
s = "abcd"
print(Solution().longestDupSubstring(s))
