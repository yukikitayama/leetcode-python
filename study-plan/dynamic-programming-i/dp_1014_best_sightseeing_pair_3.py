from typing import List


# class Solution:
#     def maxScoreSightseeingPair(self, values: List[int]) -> int:
#         ans = 0
#
#         for i in range(len(values)):
#             for j in range(i + 1, len(values)):
#
#                 score = values[i] + values[j] + i - j
#                 ans = max(ans, score)
#
#         return ans


"""
- distance
  - 1 <= distance <= (len(values) - 1)
- values: [8, 1, 5, 2, 6]
  - i: 0, j: 1, values[i]: 8, values[j]: 1, score: 8 + 1 + 0 - 1 = 8
  - i: 0, j: 2, because values[2] is bigger than values[1]
                values[i]: 8, values[j]: 5, score: 8 + 5 + 0 - 2 = 11
    - But if values[2] is 1, we should not use j: 2, because we have negative distance impact
    - i: 0, j: 2, suppose values[2]: 1, score: 8 + 1 + 0 - 2 = 7, which is smaller score
    - We should move j if it offsets distance negative impact. 
- track left max so far, and right max so far?
  - left max so far is values[i] + i
  - right max so far is values[j] - j
  - i < j
  - i iterates from 0 to len(values) - 2
  - j iterates from 1 to len(values) - 1
  
Algorithm
- Initialize ans to 0
- Scan from left to right
  - ans = max(ans, curr_score)
"""


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Score = values[i] + values[j] + i - j
        #       = values[i] + i + values[j] - j

        # See the below as values[i] + i
        max_so_far = values[0] + 0
        ans = 0

        for j in range(1, len(values)):
            # Update score if updating max_so_far with the current values[j] - j is good
            ans = max(ans, max_so_far + values[j] - j)
            # Update previous values[i] + i if current values[i] + i is good
            # See the below j as using i in my mind
            max_so_far = max(max_so_far, values[j] + j)

        return ans


values = [8, 1, 5, 2, 6]
# values = [1,2]
print(Solution().maxScoreSightseeingPair(values))
