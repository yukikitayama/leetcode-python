"""
Always get the second largest
Max heap
"""

from typing import List
import heapq
import collections


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)

        ans = 0

        curr = 0

        while max_heap:

            curr_pile = heapq.heappop(max_heap)

            if curr == 1:
                ans += - curr_pile

            curr += 1
            curr %= 3

        return ans


class Solution2:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = collections.deque(piles)

        ans = 0

        while queue:

            bob = queue.popleft()
            alice = queue.pop()
            ans += queue.pop()

        return ans


class Solution3:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0

        # the first n // 3 items are taken by bob, so we start from after that
        # 6 // 3 = 2,
        for i in range(len(piles) // 3, len(piles), 2):
            ans += piles[i]

        return ans


if __name__ == "__main__":
    piles = [2, 4, 1, 2, 7, 8]  # 9
    # piles = [2, 4, 5]  # 4
    piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]  # 18
    print(Solution2().maxCoins(piles))
