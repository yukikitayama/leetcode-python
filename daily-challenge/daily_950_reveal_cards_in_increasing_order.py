"""
sort deck
from the largest element, reconstruct the deck in reverse
  popright from the queue and append left it to the queue
  append left the current num

I didn't use the info all values are unique
"""

from typing import List
import collections


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = collections.deque([i for i in range(len(deck))])
        deck.sort()
        ans = [0] * len(deck)
        for i in range(len(deck)):
            idx = queue.popleft()

            ans[idx] = deck[i]

            if i == len(deck) - 1:
                return ans

            next_idx = queue.popleft()
            queue.append(next_idx)

    def deckRevealedIncreasing1(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = collections.deque()
        i = len(deck) - 1
        while i >= 0:
            num = deck[i]
            i -= 1

            if not queue:
                queue.append(num)

            else:
                right_num = queue.pop()
                queue.appendleft(right_num)
                queue.appendleft(num)

        return list(queue)