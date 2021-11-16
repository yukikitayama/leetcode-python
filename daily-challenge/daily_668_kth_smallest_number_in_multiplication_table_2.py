"""
- Heap
- TLE
"""


import heapq


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        mat = []
        for row in range(1, m + 1):
            line = []
            for col in range(1, n + 1):
                line.append(row * col)
            mat.append(line)
        [print(row) for row in mat]

        # Heap contains the smallest unused element of each row
        # (val, root)
        # val: next unused value for that row
        # root: starting value of that row
        heap = [(i, i) for i in range(1, m + 1)]
        heapq.heapify(heap)

        print(f'Starting heap: {heap}')

        for i in range(k):

            print(f'  i: {i}')

            val, root = heapq.heappop(heap)
            # nxt can be calculated by adding root
            # because each row is a factor of root
            # root: 2 means the current row is 2, 4, 6, 8, ...
            # val is the next unused value, so by adding 2 to val,
            # we can get the next value e.g. val: 4, root: 2, nxt: 6
            nxt = val + root

            print(f'  val: {val}, root: {root}, nxt: {nxt}, root * n: {root * n}')

            # root * n?
            # nxt could be out of boundary by m * n matrix
            # root * n is the maximum allowed value for a row starting with root
            # e.g. m: 3, n:3, heap popped val: 3, root: 1,
            # nxt is 4 because val + root = 3 + 1 = 4
            # but 4 is not allowed because matrix is 3 by 3
            # So this only push allowed value to heap
            if nxt <= root * n:
                heapq.heappush(heap, (nxt, root))

            print(f'    heap: {heap}')

        return val


"""
- Heap size is m, because of each row, so heappush and pop takes O(logm),
  but it first push m element to heap, so O(mlogm)
  we do it for k, so time is O(kmlogm)
- Space is m for the heap
"""


m = 3
n = 3
k = 5
# m = 2
# n = 3
# k = 6
print(Solution().findKthNumber(m, n, k))

