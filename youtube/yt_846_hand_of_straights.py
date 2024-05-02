"""
hand length needs to be divisible by groupSize
  if not, false

sort
min heap
hashmap
"""

from typing import List
import collections


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        counter = collections.Counter(hand)
        hand.sort()

        for i in range(len(hand)):

            curr = hand[i]

            if curr not in counter:
                continue

            for j in range(groupSize):

                if curr in counter:
                    counter[curr] -= 1
                    if counter[curr] == 0:
                        del counter[curr]

                else:
                    return False

                curr += 1

        return True