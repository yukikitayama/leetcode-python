import collections


class FrontMiddleBackQueue:

    def __init__(self):
        self.first_half = collections.deque()
        self.second_half = collections.deque()

    def pushFront(self, val: int) -> None:
        # Entire front is the start of first half
        self.first_half.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.first_half) > len(self.second_half):
            # If first half is too big, move one from first half end to second half start
            self.second_half.appendleft(self.first_half.pop())
        # To be middle, put it to end of first half
        self.first_half.append(val)
        # Here first half is equal size to second half or longer by one

    def pushBack(self, val: int) -> None:
        self.second_half.append(val)
        self.balance()

    def popFront(self) -> int:
        val = self.first_half.popleft() if self.first_half else -1
        self.balance()
        return val

    def popMiddle(self) -> int:
        val = self.first_half.pop() if self.first_half else -1
        self.balance()
        return val

    def popBack(self) -> int:
        val = -1
        if self.second_half:
            val = self.second_half.pop()
        elif self.first_half:
            val = self.first_half.pop()
        self.balance()
        return val

    def balance(self):
        # Keep relationship of first half length >= second half
        if len(self.first_half) > len(self.second_half) + 1:
            # Move first half end to second half start
            self.second_half.appendleft(self.first_half.pop())
        if len(self.first_half) < len(self.second_half):
            # Move second half start to first half end
            self.first_half.append(self.second_half.popleft())


class FrontMiddleBackQueue1:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(len(self.queue) // 2, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        return self.queue.pop(0) if self.queue else -1

    def popMiddle(self) -> int:
        return self.queue.pop((len(self.queue) - 1) // 2) if self.queue else -1

    def popBack(self) -> int:
        return self.queue.pop() if self.queue else -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()