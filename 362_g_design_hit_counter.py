from collections import deque


class HitCounter:
    def __init__(self):
        self.hits = deque([])

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while len(self.hits) > 0:
            # e.g. hits[1, 2, 3], timestamp: 4, hits[0]: 1, diff: 3
            # e.g. hits[1, 2, 3, 300], timestamp: 301, hits[0]: 1, diff: 300, if: T, hits: [2, 3, 300], hits[0]: 2,
            #      diff: 301 - 2 = 299, if: F, break, len(hits): 3
            diff = timestamp - self.hits[0]
            if diff >= 300:
                self.hits.popleft()
            else:
                break

        return len(self.hits)


obj = HitCounter()
print(obj.hit(1))
print(obj.hit(2))
print(obj.hit(3))
print(obj.getHits(4))
print(obj.hit(300))
print(obj.getHits(300))
print(obj.getHits(301))
