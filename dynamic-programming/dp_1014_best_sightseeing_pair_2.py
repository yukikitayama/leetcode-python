from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Keeps ith sightseeing spot max value so far
        current_max_i = values[0]
        # The maximum score of a pair of sightseeing splots to return
        answer = 0

        for i in range(1, len(values)):
            # Image value[i] - i is the jth sightseeing spot score even if it uses i
            answer = max(answer, current_max_i + values[i] - i)
            # To make one pass possible, keep the max ith sightseeing spot score
            current_max_i = max(current_max_i, values[i] + i)

        return answer


# values = [8,1,5,2,6]
values = [1,2]
print(Solution().maxScoreSightseeingPair(values))
