class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten list of lists into a list
        intervals = [i for s in schedule for i in s]

        # Sort by start time
        intervals = sorted(intervals, key=lambda x: x.start)

        # for interval in intervals:
        #     print(f'interval.start: {interval.start}, interval.end: {interval.end}')

        ans = []

        # Initialize current interval
        pre = intervals[0]

        for curr in intervals[1:]:

            # Merge intervals
            if curr.start <= pre.end < curr.end:
                pre.end = curr.end

            # If we find an empty interval
            elif curr.start > pre.end:
                free_time = Interval(pre.end, curr.start)
                ans.append(free_time)

                pre = curr

        return ans


if __name__ == '__main__':
    schedule = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]

    schedule = [
        [Interval(1, 3), Interval(6, 7)],
        [Interval(2, 4)],
        [Interval(2, 5), Interval(9, 12)]
    ]

    ans = Solution().employeeFreeTime(schedule)
    print()
    for interval in ans:
        print(f'interval.start: {interval.start}, interval.end: {interval.end}')
