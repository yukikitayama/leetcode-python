"""
[1,4,4,6,4]
[6,5,3,6,1]
[-5, -1, 1, 0, 3]
1
6 + (6 + 5 + 3 + 1)
4 + (6 + 5 + 3 + 6) = 4 + 20 = 24
exp: 24
"""

from typing import List
import heapq


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for i in range(len(reward1)):
            heapq.heappush(max_heap, (-1 * (reward1[i] - reward2[i]), -1 * reward1[i], i))

        # print(max_heap)

        ans = 0
        eaten = set()

        # Mouse 1
        while k and max_heap:
            diff, r, i = heapq.heappop(max_heap)
            diff *= -1
            r *= -1

            ans += r
            k -= 1
            eaten.add(i)

        # print(f"eaten: {eaten}, ans: {ans}")

        # Mouse 2
        for i in range(len(reward2)):
            if i not in eaten:
                ans += reward2[i]

        return ans

    def miceAndCheese1(self, reward1: List[int], reward2: List[int], k: int) -> int:
        available = [True] * len(reward1)
        max_heap = []
        heapq.heapify(max_heap)

        for i in range(len(reward1)):
            heapq.heappush(max_heap, (-reward1[i], i, 1))

        for i in range(len(reward2)):
            heapq.heappush(max_heap, (-reward2[i], i, 2))

        k_1 = k
        k_2 = k

        ans = 0

        while True:

            reward, index, mouse = heapq.heappop(max_heap)

            if available[index]:
                if mouse == 1:
                    if k_1 > 0:
                        ans += -1 * reward
                        available[index] = False
                        k_1 -= 1
                elif mouse == 2:
                    if k_2 > 0:
                        ans += -1 * reward
                        k_2 -= 1
                        available[index] = False

            if sum(available) == 0:
                break

            if k_1 == 0 and k_2 == 0:
                break

        return ans
