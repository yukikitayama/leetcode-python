from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def check(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        dp = [1] * len(words)
        prev = [-1] * len(words)
        max_index = 0
        for right in range(1, len(words)):
            for left in range(right):
                if (
                        check(words[left], words[right])
                        and dp[left] + 1 > dp[right]
                        and groups[left] != groups[right]
                ):
                    dp[right] = dp[left] + 1
                    # ?
                    prev[right] = left

            # ?
            if dp[right] > dp[max_index]:
                max_index = right

        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev[i]
        ans.reverse()
        return ans