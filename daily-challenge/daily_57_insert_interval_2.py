from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def insert_interval(intervals, new_interval):
            inserted = False
            intervals_inserted = intervals[:]
            for i in range(len(intervals)):
                if new_interval[0] < intervals[i][0]:
                    intervals_inserted.insert(i, new_interval)
                    inserted = True
                    break

            if not inserted:
                intervals_inserted.append(new_interval)

            return intervals_inserted

        # Insert a new interval, possibly with overlapped
        intervals = insert_interval(intervals, newInterval)

        # print(intervals)

        def overlapped(curr, interval):
            return min(curr[1], interval[1]) - max(curr[0], interval[0]) >= 0

        def merge(curr, interval):
            new = [min(curr[0], interval[0]), max(curr[1], interval[1])]
            return new

        ans = []

        i = 0
        while i < len(intervals):

            curr = intervals[i]

            # print(f'curr: {curr}')

            while i < len(intervals) and overlapped(curr, intervals[i]):
                curr = merge(curr, intervals[i])
                i += 1
                # print(f'  curr after merge: {curr}')

            i -= 1
            ans.append(curr)
            i += 1

        return ans


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    intervals = [[1, 5]]
    newInterval = [2, 7]
    print(Solution().insert(intervals, newInterval))
