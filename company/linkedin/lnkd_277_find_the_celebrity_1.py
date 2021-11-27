"""
- celebrity node does not have outgoing edge
- celebrity node has the incoming edge with the number of n - 1
  - visit each node
  - ask everybody to everybody except knows(i, i)
  - Count the number of outgoing and incoming edges for each node
  - Return true if there's node with not outgoing and n - 1 incoming
- Time is O(n^2)
"""


def knows(a: int, b: int) -> bool:
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:

        def is_celebrity(i):
            for j in range(n):
                if i == j:
                    continue
                # If i knows j , or if j does not know i, i is not celebrity
                if knows(i, j) or not knows(j, i):
                    return False

            # If it passes all the above iteration, i is celebrity
            return True

        for i in range(n):
            if is_celebrity(i):
                return i
        return -1
