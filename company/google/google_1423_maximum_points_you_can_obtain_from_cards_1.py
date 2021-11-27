"""
"""


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k) -> int:
        n = len(cardPoints)

        front_set_of_cards = [0] * (k + 1)
        rear_set_of_cards = [0] * (k + 1)

        for i in range(k):
            # prefix sum from beginning
            front_set_of_cards[i + 1] = cardPoints[i] + front_set_of_cards[i]
            # prefix sum from end
            rear_set_of_cards[i + 1] = cardPoints[n - i - 1] + rear_set_of_cards[i]

            # print(f'i: {i}, n - i - 1: {n - i - 1}')

        # print(f'front: {front_set_of_cards}')
        # print(f'rear: {rear_set_of_cards}')

        ans = 0
        for i in range(k + 1):
            # first elements of front_set_of_cards and rear_set_of_cards are zero
            # so the below able to have cases where no element chose from either front o rear
            # 0 front, k rear
            # 1 front, k - 1 rear
            # 2 front, k - 2 rear ...
            current_score = front_set_of_cards[i] + rear_set_of_cards[k - i]
            ans = max(ans, current_score)

            # print(f'i: {i}, k - i: {k - i}')

        return ans


cardPoints = [1,2,3,4,5,6,1]
k = 3
cardPoints = [2,2,2]
k = 2
cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7
print(Solution().maxScore(cardPoints, k))

