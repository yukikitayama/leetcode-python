"""
hand = [1,2,3,6,2,3,4,7,8]
[1, 2, 2, 3, 3, 4, 6, 7, 8]
1: 1
2: 2
3: 2
4: 1
6: 1
7: 1
8: 1
min heap
  [(value, count)]
  size counter
  heap gets empty and size is group size
    return true
"""

from typing import List
import collections
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """I didn't understand this"""
        if len(hand) % groupSize != 0:
            return False

        counter = collections.Counter(hand)

        for card in hand:

            start_card = card

            # Find start value in the sequence where current value belong to
            while counter[start_card - 1]:
                start_card -= 1

            while start_card <= card:
                while counter[start_card]:
                    for next_card in range(start_card, start_card + groupSize):
                        if not counter[next_card]:
                            return False

                        counter[next_card] -= 1

                start_card += 1

        return True

    def isNStraightHand2(self, hand: List[int], groupSize: int) -> bool:
        counter = collections.Counter(hand)
        min_heap = []
        for k in counter.keys():
            heapq.heappush(min_heap, k)
        print(min_heap)

        while min_heap:

            curr_card = min_heap[0]

            for i in range(groupSize):

                # There are no consecutive
                if counter[curr_card + i] == 0:
                    return False

                # Decrement because used
                counter[curr_card + i] -= 1

                # Remove hand value from heap if the count is 0
                if counter[curr_card + i] == 0:
                    top_card = heapq.heappop(min_heap)
                    if curr_card + i != top_card:
                        return False

        return True

    def isNStraightHand1(self, hand: List[int], groupSize: int) -> bool:
        counter = collections.Counter(hand)
        min_heap = []
        for k, v in counter.items():
            heapq.heappush(min_heap, (k, v))

        while min_heap:

            buffer = []
            prev = None
            size = groupSize
            while min_heap and size:
                hand_val, count = heapq.heappop(min_heap)
                size -= 1
                count -= 1

                # Check consecutive
                if prev is not None and prev != hand_val - 1:
                    # print('here')
                    return False
                else:
                    prev = hand_val

                # Reuse
                if count > 0:
                    buffer.append((hand_val, count))

                # print(f"{min_heap}, hand_val: {hand_val}, count: {count}, prev: {prev}, size: {size}, buffer: {buffer}")

            while buffer:
                v, c = buffer.pop()
                heapq.heappush(min_heap, (v, c))

        if size == 0:
            return True
        else:
            return False