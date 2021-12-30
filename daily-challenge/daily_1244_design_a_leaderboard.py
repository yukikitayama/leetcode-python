"""
- Hashmap
- heap
"""


import collections
import heapq


class Leaderboard:
    def __init__(self):
        self.scores = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for x in self.scores.values():
            # Min heap
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


if __name__ == '__main__':
    obj = Leaderboard()
    obj.addScore(1, 73)
    obj.addScore(2, 56)
    obj.addScore(3, 39)
    obj.addScore(4, 51)
    obj.addScore(5, 4)
    print(obj.top(1))
    obj.reset(1)
    obj.reset(2)
    obj.addScore(2, 51)
    print(obj.top(3))
