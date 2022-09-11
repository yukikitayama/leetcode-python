import collections


class HitCounter:
    def __init__(self):
        self.t_to_count = collections.defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.t_to_count[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        ans = 0

        for t in list(self.t_to_count.keys()):
            if t <= timestamp - 300:
                del self.t_to_count[t]
            else:
                ans += self.t_to_count[t]

        return ans


class HitCounter1:
    def __init__(self):
        self.queue = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        return len(self.queue)


if __name__ == '__main__':
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    print(obj.getHits(4))
    obj.hit(300)
    print(obj.getHits(300))
    print(obj.getHits(301))
