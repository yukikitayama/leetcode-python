from typing import List
import collections
import heapq


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        new_queries = collections.defaultdict(list)

        for i, (a, b) in enumerate(queries):

            # Direct jump
            if a < b and heights[a] < heights[b]:
                ans[i] = b
            elif b < a and heights[b] < heights[a]:
                ans[i] = a
            elif a == b:
                ans[i] = a

            #
            else:
                new_queries[max(a, b)].append(
                    (max(heights[a], heights[b]), i)
                )

        min_heap = []
        for i, height in enumerate(heights):

            # min_heap[0][0]: height
            while min_heap and min_heap[0][0] < height:
                _, j = heapq.heappop(min_heap)
                ans[j] = i

            if i in new_queries:
                for max_height, j in new_queries[i]:
                    heapq.heappush(min_heap, (max_height, j))

        return ans