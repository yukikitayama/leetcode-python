import collections


class MyCalendarThree:
    def __init__(self):
        self.vals = collections.Counter()
        self.lazy = collections.Counter()

    def update(self, start: int, end: int, left: int=0, right: int=10**9, idx: int=1) -> None:
        # ?
        if start > right or end < left:
            return

        if start <= left <= right <= end:
            self.vals[idx] += 1
            self.lazy[idx] += 1

        else:
            mid = (left + right) // 2
            self.update(start, end, left, mid, idx * 2)
            self.update(start, end, mid + 1, right, idx * 2 + 1)
            self.vals[idx] = self.lazy[idx] + max(self.vals[2 * idx], self.vals[2 * idx + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1)
        return self.vals[1]


class MyCalendarThree1:
    def __init__(self):
        self.diff = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.diff[start] += 1
        self.diff[end] -= 1
        ans = 0
        curr = 0
        for k, v in sorted(self.diff.items()):
            curr += v
            ans = max(ans, curr)
        return ans


if __name__ == '__main__':
    obj = MyCalendarThree()
    print(obj.book(10, 20))
    print(obj.book(50, 60))
    print(obj.book(10, 40))
    print(obj.book(5, 15))
    print(obj.book(5, 10))
    print(obj.book(25, 55))
