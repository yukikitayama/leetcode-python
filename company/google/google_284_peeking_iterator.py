from typing import List


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        pass

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        pass

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._peeked_value = None

    def peek(self):
        """
        Returns the next element in the iterator without advancing the iterator.
        :rtype: int
        """
        if not self._peeked_value:
            if not self._iterator.hasNext():
                # Signal there are no further items produced by the iterator
                raise StopIteration()
            self._peeked_value = self._iterator.next()

        return self._peeked_value

    def next(self):
        """
        :rtype: int
        """
        if self._peeked_value:
            to_return = self._peeked_value
            self._peeked_value = None
            return to_return

        if not self._iterator.hasNext():
            raise StopIteration()

        return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        # Cannot use "return self._peeked_value or self._iterator.hasNext()"
        # because if self._peeked_value can use as T or F in if statement
        # but it will return the actual value if it's used in return statement
        return self._peeked_value is not None or self._iterator.hasNext()
