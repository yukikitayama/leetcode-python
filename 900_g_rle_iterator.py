from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        # While this is true, next() can return a number in array
        # But once index gets out of the bound, return -1 to show no element left to exhaust
        while self.index < len(self.encoding):

            # n in next() is smaller or equal to the current index amount, so we exhaust
            if n <= self.encoding[self.index]:
                # next() exhausts it, so decrement by n
                self.encoding[self.index] -= n

                # number at self.index represent how many time we can exhaust
                # number at self.index + 1 is the actual number to be used
                return self.encoding[self.index + 1]

            # n exceeds the amount at current index, so go to the next index and return the next number
            # Decrement by the remaining amount at current index
            n -= self.encoding[self.index]
            # += 2 because (index + 1) is current number to return,
            # and (index + 2) is how many times to exhaust the next number
            self.index += 2

        return -1


"""
Time complexity
Let n be the number of items, O(n)
"""


obj = RLEIterator([3, 8, 0, 9, 2, 5])
# print(obj.next(2))
# print(obj.next(1))
# print(obj.next(1))
# print(obj.next(2))
print(obj.next(4))  # 5



