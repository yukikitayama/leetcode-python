from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0

        for i in range(len(colors)):

            next_ = (i + 1) % len(colors)
            next_next = (i + 2) % len(colors)

            if colors[i] == colors[next_next] and colors[i] != colors[next_]:
                ans += 1

        return ans