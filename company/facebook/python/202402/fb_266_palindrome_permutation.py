"""
1. all characters have even number of characters
2. one character has odd number of characters, and all other are evem number

Create counter
seen odd binary false
iterate key value
  if seen odd true and current key has odd value
    return False
return true
"""

import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)

        seen_odd = False

        for k, v in counter.items():

            # Odd
            if v % 2 == 1 and not seen_odd:
                seen_odd = True
            elif v % 2 == 1 and seen_odd:
                return False

        return True
