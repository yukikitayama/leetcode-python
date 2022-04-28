from typing import List
import heapq


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:

        # Make sweep line
        # Records: [(paint position index, ith day, type of painting ), ...]
        # Type of painting: 1 is start painting, -1 is end painting
        records = []

        # Inclusive paint end position
        # Later we need this to sweep all the paint position
        max_pos = 0

        for i, [start, end] in enumerate(paint):
            records.append((start, i, 1))
            records.append((end, i, -1))
            max_pos = max(max_pos, end)

        # Sort by ascending paint position, by ascending ith day
        # 3rd element type doesn't matter
        records.sort()

        # print(f'records: {records}')
        # print(f'max_pos: {max_pos}')

        ans = [0] * len(paint)

        # Min heap to contain ith day
        indexes = []

        # Set to contain ith day index
        ended_set = set()

        # Index to iterate records
        i = 0
        for pos in range(max_pos + 1):

            # print(f'pos: {pos}')

            # If current position is start or end paint position
            while i < len(records) and records[i][0] == pos:
                pos, index, type_ = records[i]

                # Add the ith day index to min heap to increment
                if type_ == 1:
                    heapq.heappush(indexes, index)
                else:
                    ended_set.add(index)

                i += 1

            # print(f'  indexes: {indexes}, ended_set: {ended_set}, i: {i}')

            # When minimum ith day is at end position
            # Remove the ith day index to stop incrementing
            while indexes and indexes[0] in ended_set:
                heapq.heappop(indexes)

            # Increment minimum ith day as long as exist
            if indexes:
                ans[indexes[0]] += 1

            # print(f'  ans: {ans}')

        return ans


if __name__ == '__main__':
    paint = [[1, 4], [4, 7], [5, 8]]
    # [3, 3, 1]
    paint = [[1, 4], [5, 8], [4, 7]]
    # [3, 3, 1]
    print(Solution().amountPainted(paint))
