"""
List node
  val
  prev
  next

Queue
  init
    size
    sentinel head
    sentinel tail
  enqueue
    increment size
  dequeue
    get next of sentinel head
    sentinel head next = this next
    decrement size
  front
    next of sentinenl head
  rear
    prev of sentinel tail
  isempty
    use size
  isfull
    use size
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k):
        self.head = None
        self.tail = None
        self.capacity = k
        self.count = 0

    def enQueue(self, value):
        if self.count == self.capacity:
            return False

        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node

        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        next_head = self.head.next
        self.head = next_head
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1

        return self.head.val

    def Rear(self) -> int:
        if self.count == 0:
            return -1

        return self.tail.val

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity


class MyCircularQueue2:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False

        # Current tail index is (head + count - 1) % capacity
        # But the insertion index will be the next to it
        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        # Increment head index acts like deleting
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

        tail = (self.head + self.count - 1) % self.capacity

        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularQueue1:

    def __init__(self, k: int):
        self.k = k
        self.curr_size = 0
        self.sentinel_head = ListNode(-1)
        self.sentinel_tail = ListNode(-1)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head

    def enQueue(self, value: int) -> bool:
        if self.curr_size == self.k:
            return False

        node = ListNode(value)

        real_tail = self.sentinel_tail.prev

        real_tail.next = node
        node.prev = real_tail

        node.next = self.sentinel_tail
        self.sentinel_tail.prev = node

        self.curr_size += 1
        return True

    def deQueue(self) -> bool:
        if self.curr_size == 0:
            return False

        real_head = self.sentinel_head.next

        self.sentinel_head.next = real_head.next
        real_head.next.prev = self.sentinel_head

        self.curr_size -= 1
        return True

    def Front(self) -> int:
        if self.curr_size == 0:
            return -1

        real_head = self.sentinel_head.next
        return real_head.val

    def Rear(self) -> int:
        # print(f"rear, curr_size: {self.curr_size}, val: {self.sentinel_tail.prev.val}")
        if self.curr_size == 0:
            return -1

        real_tail = self.sentinel_tail.prev
        return real_tail.val

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.curr_size == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()