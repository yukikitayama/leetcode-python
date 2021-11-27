"""
- Time is O(n) optimized solution
  - O(n + n) by find a candidate first O(n), and verify it O(n)
"""


def knows(a: int, b: int) -> bool:
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:

        # Takes O(n)
        def is_celebrity(i):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True

        # Takes O(n) to find the candidate
        celebrity_candidate = 0
        for i in range(1, n):
            # if candidate know someone else, candidate is not celebrity
            # but the someone else could be celebrity,
            # so update the candidate with the someone else
            if knows(celebrity_candidate, i):
                celebrity_candidate = i

        # Takes O(n) to check if the candidate is celebrity
        if is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1



