"""
- Brute force is to get pair and % 60 to be 0 by 1 for loops
- dynamic programming?

- (a + b) % 60 = 0
- ((a % 60) + (b % 60)) % 60 = 0
  - 1. a % 60 = 0 and b % 60 =0
  - 2. (a % 60) + (b % 60) = 60
"""


from typing import List
import collections


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Hashmap with key remainder and value the number of times whose remainder is the key
        # We don't have to record the actual times which produced the remainder,
        # because we are required to return the number of pairs, not the list of pairs
        remainders = collections.defaultdict(int)
        ret = 0

        for t in time:

            # If current time has remainder 0, the other time also needs to have remainder 0
            # to be (current time + previous time) % 60 == 0
            # So key in the hashmap is 0 remainder
            if t % 60 == 0:
                ret += remainders[0]

            else:
                # The collections.defaultdict(int) returns 0 if the key does not exist
                # If current time does not have remainder 0, the other time remainder
                # and the current time remainder need to sum up to 60
                # so 60 - t % 60: (current time remainder) = the other time remainder
                ret += remainders[60 - t % 60]

            remainders[t % 60] += 1

        return ret


"""
- Time is O(n) because the for loop is O(n) and finding elements in hashmap is O(1)
- Space is O(n) for hashmap
"""
time = [30,20,150,100,40]
time = [60,60,60]
print(Solution().numPairsDivisibleBy60(time))
