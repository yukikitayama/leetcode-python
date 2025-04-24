"""
t: [1, 2], duration: 5
1, 2, 3, 4, 5
  5 - 2 = 3
  last - curr > 0

t: [1, 4], duration: 2
1, 2
  2 - 4 = -2 <= 0
"""


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries) - 1):
            ans += min(
                # Overlap
                timeSeries[i + 1] - timeSeries[i],
                # Not overlap
                duration
            )
        return ans + duration