"""
Resources
- https://realpython.com/intro-to-python-threading/
- https://www.geeksforgeeks.org/synchronization-by-using-semaphore-in-python/
- https://docs.python.org/3/library/threading.html#semaphore-objects
"""


import threading
import collections


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        # Initially queue is empty. Producers start acquiring and decrementing
        # the capacity
        self.producer = threading.Semaphore(capacity)
        # Consumer semaphore starts with 0 because it can dequeue only after
        # producers enqueue elements. So consumers semaphore gets incremented
        # by producer calls consumer.release()
        self.consumer = threading.Semaphore(0)
        # Lock to allow only one either producer or consumer to update queue
        # at a time
        self.queue_lock = threading.Lock()
        # Problem says append from the left and pop from the right, but we can
        # implement our familiar deque.append (appending from right), and
        # deque.popleft (popping from left)
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        # Decrement producer semaphore
        self.producer.acquire()

        # One thread can update the queue at a time
        self.queue_lock.acquire()
        self.queue.append(element)
        self.queue_lock.release()

        # Increment consumer semaphore, allowing consumer to dequeue
        self.consumer.release()

    def dequeue(self) -> int:
        # Decrement consumer semaphore
        self.consumer.acquire()

        # One thread can update the queue at a time
        self.queue_lock.acquire()
        ans = self.queue.popleft()
        self.queue_lock.release()

        # Increment producer semaphore. Maybe before this producer used up
        # the capacity, and cannot enqueu any more, but here dequeue removed
        # one element, so it needs to tell producer can enqueue a new element,
        # by incrementing producer semaphore
        self.producer.release()

        return ans

    def size(self) -> int:
        return len(self.queue)
