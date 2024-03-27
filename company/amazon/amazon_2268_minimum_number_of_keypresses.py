"""
Only 1 button will be 2 characters
Hashmap
  k: character in s
  v: count
Characters with many counts should be button press once
After using up 9 character,
  next many counts characters are assigned button press twice
counter for all initialized to be 0
counter for button initialized to be 1
  acounter counter for all 9, counter for button increment to 2
Ans initialized to be 0
Max heap
  [(-count, character), ()]
  pop,
    counter for button multiplied by count increments ans
"""

import heapq
import collections


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        char_to_count = collections.Counter(s)

        max_heap = []
        heapq.heapify(max_heap)
        for k, v in char_to_count.items():
            heapq.heappush(max_heap, (-v, k))

        ans = 0

        counter = 0
        multiplier = 1

        while max_heap:

            count, ch = heapq.heappop(max_heap)
            count *= -1

            counter += 1

            if counter == 10:
                multiplier += 1
            elif counter == 19:
                multiplier += 1

            ans += (count * multiplier)

        return ans

