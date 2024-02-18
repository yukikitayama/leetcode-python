"""
Create counter
iterate counter key
  add key answer array
  decrement count
  delete key when 0
  return false if current character is same as the character at array last character


Character that has large number need to be sparse
From large number character
  fill answer array by skipping one space

vvvlo

Ans
  If the count of any character exceeds half the length of a string, not possible
    ceil(length / 2)
      4 / 2 = 2
      5 / 2 = 3
  Select the most frequent character that is different from previous character
"""

import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)

        max_heap = []
        heapq.heapify(max_heap)
        for k, v in counter.items():
            heapq.heappush(max_heap, (-v, k))

        ans = []

        while max_heap:

            first_count, first_char = heapq.heappop(max_heap)

            if not ans or ans[-1] != first_char:
                ans.append(first_char)
                first_count += 1
                if first_count != 0:
                    heapq.heappush(max_heap, (first_count, first_char))

            # Second character is guaranteed to be okay to append becuase last character is first_char
            else:

                # eg. aaab, ans: [a, b, a], (1, a) was popped at first, second is empty
                # eg. vvvlo, and: [v, l, v, o], (1, v) popped, but here heap is empty
                if not max_heap:
                    return ""

                second_count, second_char = heapq.heappop(max_heap)
                ans.append(second_char)
                second_count += 1
                if second_count != 0:
                    heapq.heappush(max_heap, (second_count, second_char))
                heapq.heappush(max_heap, (first_count, first_char))

        return "".join(ans)
