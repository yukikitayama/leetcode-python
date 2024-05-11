from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0

        happiness.sort(reverse=True)
        i = 0

        while k:

            ans += max(happiness[i] - i, 0)
            i += 1
            k -= 1

        return ans