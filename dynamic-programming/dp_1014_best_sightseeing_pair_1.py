from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0

        for i in range(len(values)):
            for j in range(i, len(values)):
                if i != j:
                    current_score = values[i] + values[j] + i - j
                    max_score = max(max_score, current_score)

                # print(f'max_score: {max_score}, i: {i}, j: {j}')

        return max_score


# values = [8,1,5,2,6]
values = [1,2]
print(Solution().maxScoreSightseeingPair(values))
