from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        curr = [intervals[0]]
        ans = 0

        for interval in intervals[1:]:

            if curr[-1][1] < interval[0]:
                curr.append(interval)

            else:
                ans += 1
                curr = [interval]

        return ans


if __name__ == '__main__':
    intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
    # intervals = [[1, 3], [5, 6], [8, 10], [11, 13]]
    print(Solution().minGroups(intervals))
