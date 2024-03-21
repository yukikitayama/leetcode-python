"""
[
    [1,3,11],
    [2,4,6]
]

[
    [1,3,11],
    [2,4,6]
]

Min heap
  Put first elements from all rows
"""

from typing import List
import heapq


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        # Smallest sum
        curr_sum = 0
        curr_comb = []  # Contains column index for each row
        for i in range(len(mat)):
            curr_sum += mat[i][0]
            curr_comb.append(0)

        # Edge case
        if k == 1:
            return curr_sum

        def next_combinations(curr_comb):
            ans = []

            for r in range(len(mat)):

                # Increment column index of each row
                comb = curr_comb[:]

                if comb[r] + 1 < len(mat[0]):
                    comb[r] += 1
                    ans.append(comb[:])

            return ans

        used_combinations = set()

        def add_next_combinations_to_heap(next_combs, min_heap):

            for next_comb in next_combs:

                if tuple(next_comb) not in used_combinations:
                    r = 0
                    curr_sum = 0

                    for c in next_comb:

                        curr_sum += mat[r][c]
                        r += 1

                    heapq.heappush(min_heap, (curr_sum, next_comb))
                    used_combinations.add(tuple(next_comb))

            return min_heap

        # [(sum, array_of_column_indices)]
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, (curr_sum, curr_comb))
        count = 0

        while min_heap:

            curr_sum, curr_comb = heapq.heappop(min_heap)
            next_combs = next_combinations(curr_comb)
            min_heap = add_next_combinations_to_heap(next_combs, min_heap)

            count += 1
            if count == k:
                return curr_sum
