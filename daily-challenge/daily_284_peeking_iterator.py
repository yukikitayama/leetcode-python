# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        return self._next

    def next(self):
        if not self._next:
            raise StopIteration()

        to_return = self._next
        # Update self._next because we want it to be always next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        # It looks like we return the previous, but
        # next has called before next()
        return to_return

    def hasNext(self):
        return self._next is not None


