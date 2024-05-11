from typing import List
import collections


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        queue = collections.deque()
        queue.append(deck[0])

        for i in range(1, len(deck)):
            rear = queue.pop()
            queue.appendleft(rear)
            queue.appendleft(deck[i])

        return list(queue)
