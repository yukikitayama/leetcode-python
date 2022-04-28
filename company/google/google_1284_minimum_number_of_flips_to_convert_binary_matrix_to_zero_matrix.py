"""
- Use bit mask to implement brute force
- Brute force to O(m * n) and O(2^(m * n)) to create next state bit mask
"""


from typing import List
import collections


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        # Make bit mask
        # more top left in mat, bit exist the right most
        # more bottom right in mat, bit exists the left most
        # e.g. m: 3, n: 3, i * n + j: [0, 1, 2, 3, 4, 5, 6, 7, 8]
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))

        # print(f'start: {start}')
        # print(f'bin(start): {bin(start)}')

        # Queue: [(bit mask, number of flips)]
        dq = collections.deque([(start, 0)])
        seen = {start}

        while dq:

            cur, step = dq.popleft()

            # if cur is 0, bit mask has 0 in all the bits
            if not cur:
                return step

            # Try all the cells in the grid as origin of flips
            # which affects neighbors
            for i in range(m):
                for j in range(n):

                    # Initialize next bit mask with the current bit mask
                    next_ = cur

                    # Make the next state bit mask
                    # Flip current cell and the 4 directions neighbors
                    for r, c in [(i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                        if 0 <= r < m and 0 <= c < n:

                            # ^1 will flip 0 to 1, and 1 to 0
                            # << (r * n + 1) will move a bit mask to the left if the current
                            # cell is bottom right, and to the right if the current cell is
                            # top left. From left to right row-wise
                            next_ ^= 1 << (r * n + c)

                    # If the next state bit mask has not been seen, we try
                    # Try until we try all the possible patterns
                    if next_ not in seen:
                        seen.add(next_)
                        dq.append((next_, step + 1))

        return -1


if __name__ == '__main__':
    mat = [[0, 0], [0, 1]]
    print(Solution().minFlips(mat))
