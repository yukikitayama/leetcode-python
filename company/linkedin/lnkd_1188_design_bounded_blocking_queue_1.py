"""
- https://www.geeksforgeeks.org/synchronization-by-using-semaphore-in-python/
"""


import threading
import collections


class BoundedBlockingQueue:
    def __init__(self, capacity, int):
        self.capacity = capacity
        # Semaphore can limit the access to the shared resources with limited capacity
        # The argument is the number of threads to access simultaneously, default is 1.
        self.pushing = threading.Semaphore(capacity)
        # The initial value is 0 because pulling (dequeue) needs to happen after pushing (enqueue)
        # enqueue() does pulling.release(), which increments pulling Semaphore, and it allows dequeue()
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire()

        self.queue.append(element)

        self.editing.release()
        # enqueue() does pulling.release() because after appending elements, it can pop
        self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()

        res = self.queue.popleft()

        self.editing.release()
        # dequeue() does pushing.release() because pushing semaphore hits the limit by the capacity
        # but by dequeue an element, there is one more space to append possible in queue
        # so it allows pushing to enqueue a new element, so pushing.release() happens here
        self.pushing.release()
        return res

    def size(self) -> int:
        return len(self.queue)
