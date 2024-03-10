"""
apple = [1,3,2], capacity = [4,3,1,5,2]

Sort capacity in descending order
pointer to capacity
  decrement current capacity by current apply
    if current apple is bigger than capacity
      make current capacity zero move to next pointer

Sum of apples
  iterate capacity
  break when apple is 0

num_apple: 6
capacity: [5, 4, 3, 2, 1]
"""

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        num_apple = sum(apple)

        capacity.sort(reverse=True)

        i = 0

        while num_apple > 0:
            num_apple -= capacity[i]
            i += 1

        return i