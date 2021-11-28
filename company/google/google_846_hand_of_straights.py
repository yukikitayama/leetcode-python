from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        # print(sorted(c))
        # print(c)

        # Get sorted keys of Counter dictionary
        for i in sorted(c):

            # if c[i] is zero, it's already used for other numbers to make a straight, so no need to consider
            # If it's more than zero, in the following for loop, we need to find a straight
            if c[i] > 0:

                # groupSize: 3, range: (2, 1, 0)
                # i: 1
                # j: 2, c[i + j] = c[3] =
                # Get index to make a straight
                # This does by reverse order, but you can't do with a normal order
                # because in that case -= c[i] would be -= 0, and we can't correctly decrement them
                for j in range(groupSize - 1, -1, -1):
                    # Because using the current card, decrement it to check for the next iteration whether still can
                    # make a straight
                    c[i + j] -= c[i]

                    # If the card to make a straight does not exist in Counter, Counter will make a new key with the
                    # non existing card with initial value 0, but decrement it to -1, and we can return False
                    if c[i + j] < 0:
                        return False
        return True


"""
If we make a dictionary with collections.Counter, even if you do some operation to a key which does not exist in the
Counter dictionary, Counter will make a new key.

Time complexity
Let n be the length of hand, and m be the group size
O(nlogn + nm) because nlogn to sort the array and we have nested for loop

Space complexity
O(n) for hashmap
"""


hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
# hand = [1,2,3,4,5]
# groupSize = 4
print(Solution().isNStraightHand(hand, groupSize))
