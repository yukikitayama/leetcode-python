"""
"""


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k) -> int:
        front_sum = 0
        rear_sum = 0
        n = len(cardPoints)

        for i in range(k):
            front_sum += cardPoints[i]

        ans = front_sum
        # k: 3, n: 7
        # front i: (2, 1, 0)
        # rear: (6, 5, 4) = (n - 1, n - 2, n - 3) = (n - (k - i))
        # = (7 - (3 - 2), 7 - (3 - 1), 7 - (3 - 0))
        # = (6, 5, 4)
        for i in range(k - 1, -1, -1):
            front_sum -= cardPoints[i]
            rear_sum += cardPoints[n - (k - i)]
            summed = front_sum + rear_sum
            ans = max(ans, summed)

        return ans


"""
Test
cardPoints: [1,2,3,4,5,6,1], k: 3
front_sum: 6
ans: 6
i: 2, front_sum: 3, rear_sum: 1, summed: 4, ans: 6
i: 1, front_sum: 1, rear_sum: 7, summed: 8, ans: 8
i: 0, front_sum: 0, rear_sum: 12, summed: 12, ans: 12
"""


cardPoints = [1,2,3,4,5,6,1]
k = 3
# cardPoints = [2,2,2]
# k = 2
# cardPoints = [9, 7, 7, 9, 7, 7, 9]
# k = 7
print(Solution().maxScore(cardPoints, k))

