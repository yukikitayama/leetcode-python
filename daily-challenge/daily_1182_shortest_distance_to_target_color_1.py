from typing import List
import collections
import bisect


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_to_index = collections.defaultdict(list)

        for i, c in enumerate(colors):
            color_to_index[c].append(i)

        query_results = []

        for i, (target, color) in enumerate(queries):

            if color not in color_to_index:
                query_results.append(-1)
                continue

            index_list = color_to_index[color]

            insert = bisect.bisect_left(index_list, target)

            left_nearest = abs(index_list[max(insert - 1, 0)] - target)
            right_nearest = abs(index_list[min(insert, len(index_list) - 1)] - target)

            query_results.append(min(left_nearest, right_nearest))

        return query_results