"""
- Apply the operation to the largest pile
- Use heap
"""


from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        # Make max heap
        piles = [-pile for pile in piles]

        heapq.heapify(piles)

        while k:

            curr = -1 * heapq.heappop(piles)

            # print(f'curr: {curr}')

            divided = int(curr / 2)

            # print(f'divided: {divided}')

            k -= 1

            heapq.heappush(piles, -1 * (curr - divided))

        return -sum(piles)


if __name__ == '__main__':
    piles = [5,4,9]
    k = 2
    # 12
    piles = [4, 3, 6, 7]
    k = 3
    # 12
    print(Solution().minStoneSum(piles, k))




