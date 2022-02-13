"""
- tail = (head + count - 1) % capacity
  - capacity is the size of array
  - count is the current number of items in the array
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:

        # Queue is full, so cannot enqueue
        if self.count == self.capacity:
            return False

        # No -1 because count is +=1 after this
        # This is for getting new tail
        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:

        # Cannot dequeue if queue is empty
        if self.count == 0:
            return False

        # % capacity to make it circular
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:

        if self.count == 0:
            return -1

        return self.queue[self.head]

    def Rear(self) -> int:

        if self.count == 0:
            return -1

        # -1 because it needs to find the current tail, not new tail
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


if __name__ == '__main__':
    obj = MyCircularQueue(k=3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.queue)
