from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        max_left_so_far = values[0]
        for i in range(1, len(values)):
            ans = max(ans, max_left_so_far + values[i] - i)
            max_left_so_far = max(max_left_so_far, values[i] + i)

        return ans

    def maxScoreSightseeingPair1(self, values: List[int]) -> int:
        max_left_so_far = []
        max_left_so_far.append(values[0])
        ans = 0

        for i in range(1, len(values)):

            right_score = values[i] - i

            ans = max(
                ans,
                max_left_so_far[-1] + right_score
            )

            max_left_so_far.append(max(
                max_left_so_far[-1],
                values[i] + i
            ))

        return ans