"""
- time: 10m
- solved: 1
- saw solution: 0
- optimized: 1
"""


from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(len(intervals) - 1):
            curr_start, curr_end = intervals[i]
            next_start, next_end = intervals[i + 1]

            if curr_end > next_start:
                return False

        return True


"""
- Sorting is O(NlogN) time and O(N) space
"""


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    intervals = [[7, 10], [2, 4]]
    print(Solution().canAttendMeetings(intervals))
