class MedianFinder:
    def __init__(self):
        self.stream_holder = []

    def addNum(self, num: int) -> None:
        self.stream_holder.append(num)

    def findMedian(self) -> float:
        self.stream_holder.sort()
        mid = len(self.stream_holder) // 2
        if len(self.stream_holder) % 2 == 0:
            return (self.stream_holder[mid - 1] + self.stream_holder[mid]) / 2
        else:
            return self.stream_holder[mid]


stream1 = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
stream2 = [[], [1], [2], [], [3], []]

sol = MedianFinder()
for s1, s2 in zip(stream1, stream2):
    if s1 == 'addNum':
        sol.addNum(s2[0])
    if s1 == 'findMedian':
        print(sol.findMedian())
