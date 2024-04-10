"""
Naive
  Simulation
    Keep iterating
    increment ans
    decrement array element
    when kth element is 0, break

Greedy
"""

from typing import List
import collections


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0

        k_ticket = tickets[k]

        for i in range(len(tickets)):

            if i <= k:
                ans += min(k_ticket, tickets[i])
            elif i > k:
                ans += min(k_ticket - 1, tickets[i])

        return ans

    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        queue = collections.deque([i for i in range(len(tickets))])

        ans = 0
        while queue:
            ans += 1
            i = queue.popleft()
            tickets[i] -= 1

            if tickets[k] == 0:
                return ans

            if tickets[i] > 0:
                queue.append(i)

        return ans

    def timeRequiredToBuy1(self, tickets: List[int], k: int) -> int:
        ans = 0

        i = 0
        while True:

            if tickets[i] > 0:
                tickets[i] -= 1
                ans += 1

            if tickets[k] == 0:
                break

            i = (i + 1) % len(tickets)

        return ans
