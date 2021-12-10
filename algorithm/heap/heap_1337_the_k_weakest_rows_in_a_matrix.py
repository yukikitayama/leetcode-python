"""
Complexity
- Let m be row, n be column
- Time
  - Get strength is O(mlogn), because for m rows, doing binary search is O(logn) for each row to have n items
  - Heap max size is k, inserting and deleting is O(logk), we try inserting for m rows, so O(mlogk)
  - In total, O(mlogn + mlogk) = O(m(logn + logk)) = O(mlognk)
"""


from typing import List
import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        heap = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)

            # bigger means smaller, because to get the k smallest, heap needs to be max heap
            if len(heap) < k or entry > heap[0]:
                heapq.heappush(heap, entry)
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        while heap:
            strength, i = heapq.heappop(heap)
            ans.append(-i)

        return ans[::-1]





