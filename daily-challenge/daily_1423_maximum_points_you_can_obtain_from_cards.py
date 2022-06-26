"""
- Stack
- Prefix sum

- Find subarray whose sum is minimize, so remaining is maximized
"""


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)

        if k == len(cardPoints):
            return total

        min_subarray_total = total

        curr_score = 0
        start = 0
        for i in range(len(cardPoints)):

            curr_score += cardPoints[i]
            curr_len = i - start + 1

            if curr_len == (len(cardPoints) - k):
                min_subarray_total = min(min_subarray_total, curr_score)
                curr_score -= cardPoints[start]
                start += 1

        return total - min_subarray_total


class Solution1:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front = [0] * (k + 1)
        rear = [0] * (k + 1)

        for i in range(k):
            front[i + 1] = front[i] + cardPoints[i]
            rear[i + 1] = rear[i] + cardPoints[len(cardPoints) - i - 1]

        # print(f'front: {front}')
        # print(f'rear: {rear}')

        ans = 0

        for i in range(k + 1):
            # starts with empty front and full rear
            # one front and full - one rear
            # ...
            curr = front[i] + rear[k - i]
            ans = max(ans, curr)

        return ans


if __name__ == '__main__':
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    cardPoints = [100, 40, 17, 9, 73, 75]
    k = 3
    # 248
    print(Solution().maxScore(cardPoints, k))
